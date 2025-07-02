"""
SQLAlchemy database integration for ArogyaMitr backend.

Defines the engine, session factory, and declarative base for ORM models.
Environment variables (eg from .env) should define the DATABASE_URL for real deployment.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# PUBLIC_INTERFACE
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./arogyamitr_dev.db")  # Use SQLite fallback for dev/mock

# SQLAlchemy ORM configuration
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()

# Dependency helper
# PUBLIC_INTERFACE
def get_db():
    """
    FastAPI dependency for SQLAlchemy sessions.
    On request: yields a session and closes it after.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
