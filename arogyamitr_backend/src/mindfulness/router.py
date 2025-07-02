"""Mindfulness endpoints: meditation, mood logging."""

from fastapi import APIRouter, Depends, HTTPException
from ..mindfulness.schemas import MeditationSession, MoodLog
from ..users.service import get_current_active_user
from ..users.schemas import UserProfile

router = APIRouter(prefix="/mindfulness", tags=["Mindfulness"])

# PUBLIC_INTERFACE
@router.get("/meditations", response_model=list[MeditationSession], summary="Meditation session logs")
async def list_meditations(current_user: UserProfile = Depends(get_current_active_user)):
    """
    Returns mock meditation session logs for the user.

    These mock sessions are for demo purposes. Replace with real DB data.
    """
    return [
        MeditationSession(id=1, user_id=current_user.id, duration_minutes=15, technique="Mindful Breathing", mood_before="anxious", mood_after="relaxed"),
        MeditationSession(id=2, user_id=current_user.id, duration_minutes=10, technique="Body Scan", mood_before="neutral", mood_after="calm"),
        MeditationSession(id=3, user_id=current_user.id, duration_minutes=20, technique="Guided Meditation", mood_before="tired", mood_after="rejuvenated"),
    ]

# PUBLIC_INTERFACE
@router.post("/mood", response_model=MoodLog, summary="Log mood/journal entry")
async def create_mood_log(mood: MoodLog, current_user: UserProfile = Depends(get_current_active_user)):
    """Stub: accept mood log journal entry."""
    if mood.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="User mismatch.")
    return mood
