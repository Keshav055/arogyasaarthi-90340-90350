from pydantic import BaseModel
from typing import Optional

# PUBLIC_INTERFACE
class AppointmentRequest(BaseModel):
    """Schema for booking a teleconsultation appointment."""
    user_id: int
    doctor_id: int
    scheduled_time: str
    reason: Optional[str] = None

# PUBLIC_INTERFACE
class DoctorProfile(BaseModel):
    """Schema for a doctor's profile."""
    id: int
    name: str
    specialization: str
    experience_years: Optional[int] = None
