"""Service logic for user CRUD and retrieval."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from typing import Optional, Dict
from ..users import schemas as user_schemas
import os

fake_users_db: Dict[str, user_schemas.UserProfile] = dict()  # Simulated DB: email -> user

OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="/auth/login")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "DO_NOT_USE_IN_PROD")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

# PUBLIC_INTERFACE
async def get_user_by_email(email: str) -> Optional[user_schemas.UserProfile]:
    """Get user from fake DB (by email)."""
    return fake_users_db.get(email)

# PUBLIC_INTERFACE
async def add_user_to_db(user: user_schemas.UserProfile):
    """Add a new user profile to the fake DB (simulate)."""
    fake_users_db[user.email] = user
    return user

# PUBLIC_INTERFACE
async def get_user_by_id(user_id: int) -> Optional[user_schemas.UserProfile]:
    """Fetch user by id from fake DB."""
    for user in fake_users_db.values():
        if user.id == user_id:
            return user
    return None

# PUBLIC_INTERFACE
async def get_current_active_user(token: str = Depends(OAUTH2_SCHEME)) -> user_schemas.UserProfile:
    """Decode JWT and fetch user record."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id: int = int(payload.get("sub"))
    except (JWTError, ValueError):
        raise credentials_exception
    user = await get_user_by_id(user_id)
    if not user:
        raise credentials_exception
    return user

# PUBLIC_INTERFACE
async def update_profile(user_id: int, update: user_schemas.UserUpdate):
    """Update user profile in fake DB."""
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    for field, value in update.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    fake_users_db[user.email] = user
    return user

# PUBLIC_INTERFACE
async def delete_profile(user_id: int):
    """Delete user from fake DB."""
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    del fake_users_db[user.email]
    return {"msg": "User deleted."}
