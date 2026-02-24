from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

DB_USER = "root"
DB_PASSWORD = quote_plus("#Raksha@123")  # ONLY this
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "student_db"

# Server URL (no database yet)
server_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"

engine = create_engine(server_url)

# Create database if not exists
with engine.begin() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))

# Database URL
DATABASE_URL = f"{server_url}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()