from typing import Optional
from app.db.config_db import DatabaseConnection
from app.shared.decorators.query_reader import sql_query_reader
import os
from typing import List, Dict

base_dir = os.path.dirname(os.path.abspath(__file__))

class UserQueries:
    @sql_query_reader(base_dir, "get_all_users.sql") 
    def get_all_users(self, conn: DatabaseConnection,) -> List[Dict]:
        query: str = self.get_all_users.query

        resp = conn.execute_query(query)

        return resp
    
    @sql_query_reader(base_dir, "get_user.sql")
    def get_user(
        self,
        conn: DatabaseConnection,
        id: int,
    ) -> Optional[dict]:

        query: str = self.get_user.query
        params = (id,)
        resp = conn.execute_query(query, params)
        return resp

    @sql_query_reader(base_dir, "insert_user.sql")
    def insert_user(
        self, nombre: str, conn: DatabaseConnection
    ) -> Optional[int]:
        query: str = self.insert_user.query
        params = (nombre,) 
        resp = conn.execute_update(query, params)
        return resp