from pydantic import BaseModel, EmailStr, Field

# PUBLIC_INTERFACE
class LoginRequest(BaseModel):
    """Schema for login requests."""
    email: EmailStr = Field(..., description="User's email")
    password: str = Field(..., description="User's password")


# PUBLIC_INTERFACE
class SignupRequest(BaseModel):
    """Schema for signup requests."""
    email: EmailStr = Field(..., description="User's email")
    password: str = Field(..., description="User's password")
    name: str = Field(..., description="User's full name")


# PUBLIC_INTERFACE
class TokenResponse(BaseModel):
    """Schema for authentication token response."""
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field("bearer", description="Type of token")
