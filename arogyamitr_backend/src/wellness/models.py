"""
ORM models for Wellness domain.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

# PUBLIC_INTERFACE
class WellnessTip(Base):
    """ORM table for wellness tips."""
    __tablename__ = "wellness_tips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

# PUBLIC_INTERFACE
class WellnessPathSelection(Base):
    """ORM table for user-selected wellness paths."""
    __tablename__ = "wellness_path_selections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    selected_path = Column(String, nullable=False)
