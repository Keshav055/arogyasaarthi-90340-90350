"""Nutrition & Diet endpoints: meal plans, meals."""

from fastapi import APIRouter, Depends
from ..nutrition.schemas import NutritionPlan, Meal
from ..users.service import get_current_active_user
from ..users.schemas import UserProfile

router = APIRouter(prefix="/nutrition", tags=["Nutrition & Diet"])

# PUBLIC_INTERFACE
@router.get("/plans", response_model=list[NutritionPlan], summary="List nutrition plans")
async def list_nutrition_plans(current_user: UserProfile = Depends(get_current_active_user)):
    """Return stubbed nutrition plans."""
    return [
        NutritionPlan(id=1, user_id=current_user.id, title="Healthy Veg Plan", meals=["breakfast", "lunch", "dinner"]),
        NutritionPlan(id=2, user_id=current_user.id, title="High Protein Diet", meals=["breakfast", "snack", "lunch", "dinner"]),
    ]

# PUBLIC_INTERFACE
@router.get("/meals", response_model=list[Meal], summary="List meals with macro info")
async def list_meals(current_user: UserProfile = Depends(get_current_active_user)):
    """Return stubbed meals with calories/nutrients."""
    return [
        Meal(name="Paneer Bhurji", calories=250, nutrients={"protein": "15g", "carbs": "10g", "fat": "18g"}),
        Meal(name="Masala Oats", calories=180, nutrients={"protein": "5g", "carbs": "28g", "fiber": "4g"})
    ]
