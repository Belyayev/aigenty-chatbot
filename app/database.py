import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=mls-data.database.windows.net;PORT=1433;DATABASE=MLS_data;UID=aigentymvp;PWD=ghpdGypWzGNGRh1AxKEA;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
def get_db_connection():
    return pyodbc.connect(DATABASE_URL)
