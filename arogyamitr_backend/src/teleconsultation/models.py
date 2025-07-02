"""
ORM models for Teleconsultation domain.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

# PUBLIC_INTERFACE
class AppointmentRequest(Base):
    """ORM table for teleconsult appointments."""
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    scheduled_time = Column(String, nullable=False)
    reason = Column(String, nullable=True)

# PUBLIC_INTERFACE
class DoctorProfile(Base):
    """ORM table for doctor profiles."""
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    experience_years = Column(Integer, nullable=True)
