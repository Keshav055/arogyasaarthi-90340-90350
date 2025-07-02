"""
ORM models for Disease Management domain.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from ..database import Base

# PUBLIC_INTERFACE
class VitalsRecord(Base):
    """ORM table for user health vitals."""
    __tablename__ = "vitals_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(String, nullable=False)
    blood_pressure = Column(String, nullable=True)
    heart_rate = Column(Integer, nullable=True)
    blood_sugar = Column(Float, nullable=True)
    weight = Column(Float, nullable=True)

# PUBLIC_INTERFACE
class DiseaseLog(Base):
    """ORM table for disease event/logs."""
    __tablename__ = "disease_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    condition = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    timestamp = Column(String, nullable=True)
