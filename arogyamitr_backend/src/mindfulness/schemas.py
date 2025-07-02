from pydantic import BaseModel
from typing import Optional

# PUBLIC_INTERFACE
class MeditationSession(BaseModel):
    """Schema for a meditation session log."""
    id: int
    user_id: int
    duration_minutes: int
    technique: Optional[str] = None
    mood_before: Optional[str] = None
    mood_after: Optional[str] = None

# PUBLIC_INTERFACE
class MoodLog(BaseModel):
    """Schema for logging a user's mood/journal entry."""
    user_id: int
    mood: str
    note: Optional[str] = None
    timestamp: Optional[str] = None
