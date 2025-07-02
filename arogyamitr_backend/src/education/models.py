"""
ORM models for Education Hub domain.
"""

from sqlalchemy import Column, Integer, String
from ..database import Base

# PUBLIC_INTERFACE
class Article(Base):
    """ORM table for educational articles."""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    author = Column(String, nullable=True)
    published_at = Column(String, nullable=True)

# PUBLIC_INTERFACE
class ResourceVideo(Base):
    """ORM table for educational/resource videos."""
    __tablename__ = "resource_videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(String, nullable=True)
    duration_seconds = Column(Integer, nullable=True)
