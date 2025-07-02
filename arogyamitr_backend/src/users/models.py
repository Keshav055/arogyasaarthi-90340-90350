"""
SQLAlchemy ORM model for the User entity.
"""

from sqlalchemy import Column, Integer, String
from ..database import Base

# PUBLIC_INTERFACE
class User(Base):
    """User account ORM model for authentication and profile data."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
