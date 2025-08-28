import pyodbc
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class DatabaseConnection:
    def __init__(self):
        self.driver = os.getenv("ODBC_DRIVER", "ODBC Driver 17 for SQL Server")
        self.db_host = os.getenv("DATABASE_HOST", "localhost")
        self.db_user = os.getenv("DATABASE_USER", "")
        self.db_password = os.getenv("DATABASE_PASSWORD", "")
        self.db_database = os.getenv("DATABASE_NAME", "")
        self.db_port = os.getenv("DATABASE_PORT", "1433")

        if "\\" in self.db_host:
            server = self.db_host
        else:
            server = f"{self.db_host},{self.db_port}"

        # Si no hay user/password -> Windows Auth
        if self.db_user and self.db_password:
            auth = f"UID={self.db_user};PWD={self.db_password};"
        else:
            auth = "Trusted_Connection=yes;"

        self.conn_str = (
            f"DRIVER={{{self.driver}}};"
            f"SERVER={server};"
            f"DATABASE={self.db_database};"
            f"{auth}"
            "Encrypt=no;TrustServerCertificate=yes;"
        )

    def connect(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            return conn, cursor
        except Exception as e:
            print("Error de conexión:", e)
            return None, None

    def close(self, conn, cursor):
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    def execute_query(self, query, params=None):
        connection, cursor = self.connect()
        if not connection or not cursor:
            return None
        try:
            cursor.execute(query, params or ())
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            data = [dict(zip(columns, row)) for row in rows]
            logger.info("Query executed successfully: %s", query)
            return data
        except Exception as err:
            logger.error("Error executing query: %s", err)
            return None
        finally:
            self.close(connection, cursor)
    
    def execute_update(self, query, params=None):
        connection, cursor = self.connect()
        if not connection or not cursor:
            return False
        try:
            cursor.execute(query, params)
            connection.commit()
            logger.info("Update executed and committed successfully: %s", query)
            return True
        except Exception as err:
            logger.error("Error executing update: %s", err)
            connection.rollback() 
            return False
        finally:
            self.close(connection, cursor)