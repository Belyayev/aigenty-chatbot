import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_NAME')};"
    f"UID={os.getenv('DB_USER')};"
    f"PWD={os.getenv('DB_PASSWORD')};"
    "Encrypt=yes;"
)

def get_db_connection():
    return pyodbc.connect(DATABASE_URL)
