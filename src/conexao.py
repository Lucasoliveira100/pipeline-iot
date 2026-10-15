# Conexão com o PostgreSQL usada pelos outros scripts
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()  # lê o arquivo .env (a senha não vai pro GitHub)


def criar_conexao():
    # URL.create evita problema quando a senha tem caractere especial (@, #, etc.)
    url = URL.create(
        "postgresql+psycopg2",
        username=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=int(os.getenv("POSTGRES_PORT", "5432")),
        database=os.getenv("POSTGRES_DB", "iot"),
    )
    return create_engine(url)
