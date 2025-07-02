"""User profile management endpoints: read/update/delete user."""

from fastapi import APIRouter, Depends
from .service import (
    get_current_active_user,
    update_profile,
    delete_profile,
)
from ..users import schemas as user_schemas_mod

router = APIRouter(prefix="/users", tags=["Users"])

# PUBLIC_INTERFACE
@router.get("/me", response_model=user_schemas_mod.UserProfile, summary="Get profile", description="View your own user profile.")
async def get_me(current_user: user_schemas_mod.UserProfile = Depends(get_current_active_user)):
    """Get current user profile."""
    return current_user

# PUBLIC_INTERFACE
@router.put("/me", response_model=user_schemas_mod.UserProfile, summary="Update profile", description="Update your profile details.")
async def update_me(update: user_schemas_mod.UserUpdate, current_user: user_schemas_mod.UserProfile = Depends(get_current_active_user)):
    """Update profile fields for current user."""
    return await update_profile(current_user.id, update)

# PUBLIC_INTERFACE
@router.delete("/me", summary="Delete account", description="Delete your account.")
async def delete_me(current_user: user_schemas_mod.UserProfile = Depends(get_current_active_user)):
    """Delete current user account."""
    return await delete_profile(current_user.id)
