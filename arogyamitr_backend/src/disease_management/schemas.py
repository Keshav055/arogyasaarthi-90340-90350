from pydantic import BaseModel
from typing import Optional

# PUBLIC_INTERFACE
class VitalsRecord(BaseModel):
    """Schema for recording user's vitals."""
    user_id: int
    date: str
    blood_pressure: Optional[str] = None
    heart_rate: Optional[int] = None
    blood_sugar: Optional[float] = None
    weight: Optional[float] = None

# PUBLIC_INTERFACE
class DiseaseLog(BaseModel):
    """Schema for a disease management log entry."""
    user_id: int
    condition: str
    notes: Optional[str] = None
    timestamp: Optional[str] = None
