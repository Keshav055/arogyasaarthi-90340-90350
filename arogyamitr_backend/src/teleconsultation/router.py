"""Teleconsultation endpoints: appointments & doctors."""

from fastapi import APIRouter, Depends, HTTPException
from ..teleconsultation.schemas import AppointmentRequest, DoctorProfile
from ..users.service import get_current_active_user
from ..users.schemas import UserProfile

router = APIRouter(prefix="/teleconsult", tags=["Teleconsultation"])

# PUBLIC_INTERFACE
@router.get("/doctors", response_model=list[DoctorProfile], summary="List doctors")
async def list_doctors(current_user: UserProfile = Depends(get_current_active_user)):
    """Return mock list of doctors."""
    return [
        DoctorProfile(id=101, name="Dr. Aarti Sharma", specialization="General Medicine", experience_years=12),
        DoctorProfile(id=102, name="Dr. Ajay Patel", specialization="Endocrinology", experience_years=8),
    ]


# PUBLIC_INTERFACE
@router.post("/appointments", response_model=AppointmentRequest, summary="Book an appointment")
async def book_appointment(request: AppointmentRequest, current_user: UserProfile = Depends(get_current_active_user)):
    """Stub: accept appointment request (returns echo of input)."""
    if request.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="User mismatch.")
    return request
