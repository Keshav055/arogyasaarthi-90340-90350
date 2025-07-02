"""Fitness endpoints: log activities, retrieve goals."""

from fastapi import APIRouter, Depends
from ..fitness.schemas import FitnessActivity, FitnessGoal
from ..users.service import get_current_active_user
from ..users.schemas import UserProfile

router = APIRouter(prefix="/fitness", tags=["Fitness"])

# PUBLIC_INTERFACE
@router.get("/activities", response_model=list[FitnessActivity], summary="List fitness activities")
async def list_activities(current_user: UserProfile = Depends(get_current_active_user)):
    """
    Returns a list of mock fitness activity logs for the currently authenticated user.

    These are mock/demo activities; replace with real DB reads in production.
    """
    return [
        FitnessActivity(id=1, user_id=current_user.id, activity_type="Running", duration_minutes=30, calories_burned=210),
        FitnessActivity(id=2, user_id=current_user.id, activity_type="Yoga", duration_minutes=45, calories_burned=120),
        FitnessActivity(id=3, user_id=current_user.id, activity_type="Cycling", duration_minutes=20, calories_burned=130),
    ]


# PUBLIC_INTERFACE
@router.get("/goals", response_model=FitnessGoal, summary="Get fitness goals")
async def get_fitness_goal(current_user: UserProfile = Depends(get_current_active_user)):
    """
    Returns user's fitness goals as mocked/demo data.

    Replace with a real user-specific DB lookup in production.
    """
    return FitnessGoal(user_id=current_user.id, target_steps=8000, target_calories=2200)
