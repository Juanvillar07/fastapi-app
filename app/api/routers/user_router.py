from fastapi import APIRouter, HTTPException
from app.core.logging import setup_logger
from app.db.config_db import DatabaseConnection
from app.entities.user.user_queries import Users
from fastapi.responses import JSONResponse
from app.api.routers.schema import UsersOut, UserOut, ForumUser
from typing import List

STATUS_OK = 200
STATUS_BAD_REQUEST = 500

router = APIRouter()
logger = setup_logger()


@router.get(
    "/getAll",
    response_model=List[UsersOut],
)
async def user_get_all():
    try:
        logger.info("Received user_get_all request")
        conn = DatabaseConnection()
        users = Users(conn)

        status, data = users.get_all_users()

        if status != STATUS_OK:
            return JSONResponse(status_code=status, content=data)

        return data

    except Exception as e:
        logger.error(f"Error in get user_get_all: {e}")
        raise HTTPException(status_code=STATUS_BAD_REQUEST, detail=f"Get failed: {e}")


@router.get(
    "/{id}",
    response_model=UserOut,
)
async def user_get(id: int):
    try:
        conn = DatabaseConnection()
        logger.info(f"Received user_get request for ID: {id}")
        users = Users(conn)

        status, content = users.get_user(id=id)

        if status != STATUS_OK:
            return JSONResponse(status_code=status, content=content)

        logger.info(f"User retrieved successfully for ID: {id}")
        return UserOut(**content[0])

    except Exception as e:
        logger.error(f"Error in user_get for ID {id}: {e}")
        raise HTTPException(
            status_code=STATUS_BAD_REQUEST, detail=f"Error retrieving user: {e}"
        )

@router.post(
    "/create",
    response_model=UserOut,
)
async def create_user(form: ForumUser):
    try:
        logger.info("Received create_user request")
        conn = DatabaseConnection()
        users = Users(conn)

        status, message = users.insert_user(
            nombre=form.nombre,
        )

        if status != STATUS_OK:
            raise HTTPException(status_code=status, detail=message)

        return JSONResponse(status_code=201, content=message)

    except Exception as e:
        logger.error(f"Error in post insert_user: {e}")
        raise HTTPException(status_code=STATUS_BAD_REQUEST, detail=f"Get failed: {e}")
