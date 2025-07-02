from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class NutritionPlan(BaseModel):
    """Schema for a user's nutrition plan."""
    id: int
    user_id: int
    title: str
    meals: list[str] = Field(..., description="List of meals in the plan")

# PUBLIC_INTERFACE
class Meal(BaseModel):
    """Schema for detailed meal information."""
    name: str
    calories: int
    nutrients: dict
