from pydantic import BaseModel
from typing import Optional

# PUBLIC_INTERFACE
class FitnessActivity(BaseModel):
    """Schema for a fitness activity entry."""
    id: int
    user_id: int
    activity_type: str
    duration_minutes: int
    calories_burned: Optional[int] = None

# PUBLIC_INTERFACE
class FitnessGoal(BaseModel):
    """Schema for user's fitness goal."""
    user_id: int
    target_steps: Optional[int] = None
    target_calories: Optional[int] = None
