import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
def get_db_connection():
    return pyodbc.connect(DATABASE_URL)
