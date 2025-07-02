"""Authentication router for user registration, login (email/password, Google/Apple), and JWT token issuing."""

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from ..auth import schemas as auth_schemas
from ..users import schemas as user_schemas
from .service import (
    authenticate_user,
    create_user,
    create_access_token,
    oauth_login_stub,
)
from ..users.service import get_user_by_email, get_current_active_user
from datetime import timedelta
import os

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "DO_NOT_USE_IN_PROD")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

router = APIRouter(prefix="/auth", tags=["Authentication"])

# PUBLIC_INTERFACE
@router.post("/signup", response_model=user_schemas.UserProfile, summary="User registration", description="Register a new user with email and password.")
async def signup(signup_data: auth_schemas.SignupRequest):
    """Register a new user account."""
    user = await get_user_by_email(signup_data.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    created_user = await create_user(signup_data)
    return created_user


# PUBLIC_INTERFACE
@router.post("/login", response_model=auth_schemas.TokenResponse, summary="Email/password login", description="Authenticate with email and password.")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """User login with email/password, returns a JWT token."""
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password.")
    token = create_access_token(data={"sub": str(user.id)}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return auth_schemas.TokenResponse(access_token=token, token_type="bearer")


# PUBLIC_INTERFACE
@router.post("/login/social", response_model=auth_schemas.TokenResponse, summary="Social login", description="Log in with Google/Apple OAuth (stubbed).")
async def social_login(request: Request):
    """
    Social login stub endpoint for Google/Apple OAuth. Accepts JSON body with a 'provider' and 'token' fields.
    This is a placeholder implementation; replace with real OAuth validation in production.
    """
    data = await request.json()
    provider = data.get("provider")
    external_token = data.get("token")
    if provider not in ["google", "apple"] or not external_token:
        raise HTTPException(status_code=400, detail="Invalid social login request.")

    user = await oauth_login_stub(provider, external_token)
    if not user:
        raise HTTPException(status_code=401, detail=f"Unable to authenticate with {provider.title()}.")
    token = create_access_token(data={"sub": str(user.id)}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return auth_schemas.TokenResponse(access_token=token, token_type="bearer")


# PUBLIC_INTERFACE
@router.get("/me", response_model=user_schemas.UserProfile, summary="Authenticated user profile", description="Returns the profile of the current logged-in user.")
async def get_me(current_user: user_schemas.UserProfile = Depends(get_current_active_user)):
    """Returns current authenticated user's profile."""
    return current_user
