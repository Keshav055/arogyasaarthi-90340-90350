from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class WellnessTip(BaseModel):
    """Schema for a wellness tip."""
    id: int
    title: str
    description: str

# PUBLIC_INTERFACE
class WellnessPathSelection(BaseModel):
    """Schema for user choosing a wellness path."""
    user_id: int
    selected_path: str = Field(..., description="Chosen wellness path")
