import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os
def get_connection():
    return psycopg2.connect(os.getenv("DB_URL"))