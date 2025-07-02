"""
ORM models for Nutrition & Diet domain.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from ..database import Base

# PUBLIC_INTERFACE
class NutritionPlan(Base):
    """ORM table for user's nutrition plans."""
    __tablename__ = "nutrition_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    meals = Column(JSON, nullable=False)  # List of meal names/IDs

# PUBLIC_INTERFACE
class Meal(Base):
    """ORM table for meals and nutrient information."""
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    calories = Column(Integer, nullable=False)
    nutrients = Column(JSON, nullable=True)  # Dict of macro/micronutrients
