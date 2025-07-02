"""Service logic for authentication: password verification, JWT, OAuth stubs."""

from ..users import schemas as user_schemas
from ..auth import schemas as auth_schemas
from ..users.service import get_user_by_email, fake_users_db, add_user_to_db
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
import os

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "DO_NOT_USE_IN_PROD")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

# Util: Password hashing
def hash_password(password: str) -> str:
    return PWD_CONTEXT.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return PWD_CONTEXT.verify(plain, hashed)

# PUBLIC_INTERFACE
async def authenticate_user(email: str, password: str):
    """Authenticate user by email and password."""
    user = await get_user_by_email(email)
    if user and verify_password(password, user.hashed_password):
        return user
    return None

# PUBLIC_INTERFACE
async def create_user(signup_data: auth_schemas.SignupRequest):
    """Create a new user with email and hashed password."""
    hashed_pw = hash_password(signup_data.password)
    return await add_user_to_db(
        user_schemas.UserProfile(
            id=len(fake_users_db) + 1,
            email=signup_data.email,
            name=signup_data.name,
            hashed_password=hashed_pw,
            phone=None,
            age=None,
            gender=None,
            avatar_url=None,
        )
    )

# PUBLIC_INTERFACE
def create_access_token(data: dict, expires_delta: timedelta):
    """Generate a JWT token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

# PUBLIC_INTERFACE
async def oauth_login_stub(provider: str, external_token: str):
    """
    Stub for simulating social login. Accepts any non-empty external_token.
    In production, validate the external token via Google/Apple APIs and fetch user info.
    """
    # Use google_123@example.com or apple_123@example.com, depending on provider.
    email = f"{provider}_user_{external_token[:6]}@example.com"
    user = await get_user_by_email(email)
    if not user:
        # Register new user for social login if not exists
        user = await add_user_to_db(
            user_schemas.UserProfile(
                id=len(fake_users_db) + 1,
                email=email,
                name=f"{provider.capitalize()} User",
                hashed_password=hash_password("default-socialpassword"),  # Never exposed
                phone=None,
                age=None,
                gender=None,
                avatar_url=None,
            )
        )
    return user

