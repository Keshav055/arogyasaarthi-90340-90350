from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# PUBLIC_INTERFACE
class UserBase(BaseModel):
    """Base user schema."""
    email: EmailStr
    name: str = Field(..., description="User's full name")

# PUBLIC_INTERFACE
class UserProfile(UserBase):
    """Detailed user profile schema."""
    id: int
    phone: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    avatar_url: Optional[str] = None

# PUBLIC_INTERFACE
class UserUpdate(BaseModel):
    """Schema for updating user profile."""
    name: Optional[str] = None
    phone: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    avatar_url: Optional[str] = None
