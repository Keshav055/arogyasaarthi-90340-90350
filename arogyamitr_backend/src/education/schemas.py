from pydantic import BaseModel
from typing import Optional

# PUBLIC_INTERFACE
class Article(BaseModel):
    """Schema for an educational article."""
    id: int
    title: str
    summary: str
    author: Optional[str] = None
    published_at: Optional[str] = None

# PUBLIC_INTERFACE
class ResourceVideo(BaseModel):
    """Schema for an educational video resource."""
    id: int
    title: str
    url: str
    description: Optional[str] = None
    duration_seconds: Optional[int] = None
