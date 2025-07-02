"""Wellness Path & Wellness Tips endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from ..wellness.schemas import WellnessTip, WellnessPathSelection
from ..users.service import get_current_active_user
from ..users.schemas import UserProfile

router = APIRouter(prefix="/wellness", tags=["Wellness"])

# PUBLIC_INTERFACE
@router.get("/tips", response_model=list[WellnessTip], summary="List wellness tips")
async def list_wellness_tips(current_user: UserProfile = Depends(get_current_active_user)):
    """Get wellness tips for the dashboard (mocked)."""
    return [
        WellnessTip(id=1, title="Stay Hydrated", description="Drink at least 8 glasses of water a day."),
        WellnessTip(id=2, title="Morning Walk", description="A 20min brisk walk each morning boosts well-being.")
    ]


# PUBLIC_INTERFACE
@router.post("/select-path", response_model=WellnessPathSelection, summary="Select a wellness path")
async def select_wellness_path(selection: WellnessPathSelection, current_user: UserProfile = Depends(get_current_active_user)):
    """Stub: accept the chosen wellness path by user (mock acceptance)."""
    if selection.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="User mismatch.")
    return selection
