"""Education hub endpoints: articles and videos."""

from fastapi import APIRouter, Depends
from ..education.schemas import Article, ResourceVideo
from ..users.service import get_current_active_user
from ..users.schemas import UserProfile

router = APIRouter(prefix="/education", tags=["Education Hub"])

# PUBLIC_INTERFACE
@router.get("/articles", response_model=list[Article], summary="List educational articles")
async def list_articles(current_user: UserProfile = Depends(get_current_active_user)):
    """Return mock articles for the education hub."""
    return [
        Article(id=1, title="The Science of Sleep", summary="Why good sleep is crucial.", author="A. Kumar", published_at="2024-05-01"),
        Article(id=2, title="Yoga for Beginners", summary="Simple yoga asanas anyone can do.", author="P. Singh"),
    ]

# PUBLIC_INTERFACE
@router.get("/videos", response_model=list[ResourceVideo], summary="List educational videos")
async def list_videos(current_user: UserProfile = Depends(get_current_active_user)):
    """Return mock educational videos."""
    return [
        ResourceVideo(id=10, title="Healthy Indian Breakfasts", url="https://videos.arogyamitr.com/vid10", description="Quick guide to nutritious morning meals", duration_seconds=180),
        ResourceVideo(id=11, title="Pranayama Basics", url="https://videos.arogyamitr.com/vid11"),
    ]
