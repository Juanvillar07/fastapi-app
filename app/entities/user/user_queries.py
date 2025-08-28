from app.entities.user.src.queries import UserQueries
from app.db.config_db import DatabaseConnection
from typing import Tuple
# from app.api.routers.schema import UsersOut

STATUS_BAD_REQUEST = 500
STATUS_NOT_FOUND = 404
STATUS_OK = 200


class Users:
    def __init__(self, conn: DatabaseConnection):
        self.user_queries = UserQueries()
        self.conn = conn
        self.MEDIA_DIR = "users/user_files"

    def get_all_users(
        self,
    ) -> tuple:
        all_users = self.user_queries.get_all_users(
            conn=self.conn,
        )

        if not all_users:
            return STATUS_NOT_FOUND, {
                "message": "No users found for this collection"
            }

        return STATUS_OK, all_users
    
    def get_user(self, id: int) -> tuple:
        user_details = self.user_queries.get_user(conn=self.conn, id=id)

        if not user_details:
            return STATUS_NOT_FOUND, {"message": "User not found"}

        return STATUS_OK, user_details

    def insert_user(
        self, nombre: str
    ) -> Tuple[int, str]:

        resp = self.user_queries.insert_user(nombre, self.conn)
        if resp is None:
            return STATUS_BAD_REQUEST, "Failed to insert user."

        return STATUS_OK, {
            "message": "User inserted successfully",
            "status": resp,
        }
