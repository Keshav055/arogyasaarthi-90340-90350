"""Sleep tracking endpoints: demo/mock sleep logs."""

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from ..users.service import get_current_active_user
from ..users.schemas import UserProfile

router = APIRouter(prefix="/sleep", tags=["Sleep"])

# PUBLIC_INTERFACE
class SleepLog(BaseModel):
    """Schema for a user's sleep tracking entry."""
    id: int
    user_id: int
    date: str = Field(..., description="Date of sleep session (ISO date string)")
    hours_slept: float = Field(..., description="Total hours slept")
    sleep_quality: str = Field(..., description="User's subjective sleep quality rating")

# PUBLIC_INTERFACE
@router.get("/logs", response_model=list[SleepLog], summary="Sleep logs for current user")
async def list_sleep_logs(current_user: UserProfile = Depends(get_current_active_user)):
    """
    Returns mockup/demo sleep logs for the authenticated user.
    This is stub/demo data – replace with DB connection for production use.
    """
    return [
        SleepLog(id=1, user_id=current_user.id, date="2024-07-08", hours_slept=7.1, sleep_quality="good"),
        SleepLog(id=2, user_id=current_user.id, date="2024-07-07", hours_slept=5.6, sleep_quality="poor"),
        SleepLog(id=3, user_id=current_user.id, date="2024-07-06", hours_slept=8.2, sleep_quality="excellent"),
    ]
