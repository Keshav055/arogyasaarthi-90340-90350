"""
ORM models for Mindfulness domain.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

# PUBLIC_INTERFACE
class MeditationSession(Base):
    """ORM table for meditation session logs."""
    __tablename__ = "meditation_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    technique = Column(String, nullable=True)
    mood_before = Column(String, nullable=True)
    mood_after = Column(String, nullable=True)

# PUBLIC_INTERFACE
class MoodLog(Base):
    """ORM table for daily mood logs and journals."""
    __tablename__ = "mood_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    mood = Column(String, nullable=False)
    note = Column(String, nullable=True)
    timestamp = Column(String, nullable=True)
