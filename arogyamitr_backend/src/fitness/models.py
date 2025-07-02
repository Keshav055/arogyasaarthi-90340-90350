"""
ORM models for Fitness domain.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

# PUBLIC_INTERFACE
class FitnessActivity(Base):
    """ORM table for fitness activity logs."""
    __tablename__ = "fitness_activities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    activity_type = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    calories_burned = Column(Integer, nullable=True)

# PUBLIC_INTERFACE
class FitnessGoal(Base):
    """ORM table for user fitness goals."""
    __tablename__ = "fitness_goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    target_steps = Column(Integer, nullable=True)
    target_calories = Column(Integer, nullable=True)
