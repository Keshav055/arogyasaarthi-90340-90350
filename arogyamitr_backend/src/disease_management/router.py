"""Disease Management endpoints: vitals, logs."""

from fastapi import APIRouter, Depends, HTTPException
from ..disease_management.schemas import VitalsRecord, DiseaseLog
from ..users.service import get_current_active_user
from ..users.schemas import UserProfile

router = APIRouter(prefix="/disease", tags=["Disease Management"])

# PUBLIC_INTERFACE
@router.get("/vitals", response_model=list[VitalsRecord], summary="List vital records")
async def list_vitals(current_user: UserProfile = Depends(get_current_active_user)):
    """Return user vitals records (stub)."""
    return [
        VitalsRecord(user_id=current_user.id, date="2024-01-01", blood_pressure="110/70", heart_rate=70, blood_sugar=90.0, weight=68.5),
        VitalsRecord(user_id=current_user.id, date="2024-01-15", blood_pressure="115/75", heart_rate=72, blood_sugar=92.0, weight=68.0),
    ]

# PUBLIC_INTERFACE
@router.post("/log", response_model=DiseaseLog, summary="Create disease log")
async def create_disease_log(log: DiseaseLog, current_user: UserProfile = Depends(get_current_active_user)):
    """Stub: accept and return disease management log entry."""
    if log.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="User mismatch.")
    return log
