# app/services/db_service.py
import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={os.getenv('DB_HOST')},{os.getenv('DB_PORT')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')}"
        )
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco:", e)
        return None
    
import bcrypt
print("substituir senha no init.sql para testar login com o hash(Login: joao@email.com, senha: senha1234)")
hash = bcrypt.hashpw("senha1234".encode(), bcrypt.gensalt())
print(hash.decode())  # Copie este resultado
