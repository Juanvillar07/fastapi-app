from fastapi import FastAPI
from app.api.routers.user_router import router as user_router
from app.core.logging import setup_logger


logger = setup_logger()

app = FastAPI()

app.include_router(
    user_router, prefix="/users", tags=["users"]
)
