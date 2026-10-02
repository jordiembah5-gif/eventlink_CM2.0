# Chapter 1: the database connection (database.py)

# os lets us read environment variables (Render stores the database URL there)
import os

# create_engine builds the connection to the database
from sqlalchemy import create_engine

# sessionmaker makes database sessions, declarative_base makes the table blueprint
from sqlalchemy.orm import sessionmaker, declarative_base

# Use Render's DATABASE_URL if it exists, otherwise fall back to local SQLite
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./eventlink.db")

# Render gives "postgres://" but SQLAlchemy needs "postgresql://", so fix the prefix
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
        "postgres://", "postgresql://", 1
    )

# check_same_thread only exists for SQLite, so only pass it when using SQLite
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

# A session is one temporary conversation with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the blueprint that all our tables (Users, Events...) inherit from
Base = declarative_base()


# This function opens a session, hands it over, then always closes it
def get_db():
    db = SessionLocal()  # Open the conversation
    try:
        yield db  # Hand the connection to the code that requested it
    finally:
        db.close()  # Always close the connection when finished