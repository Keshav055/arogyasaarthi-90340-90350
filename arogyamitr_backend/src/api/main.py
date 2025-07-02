from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..auth.router import router as auth_router
from ..users.router import router as users_router

# Import routers for each main domain/module
from ..wellness.router import router as wellness_router
from ..nutrition.router import router as nutrition_router
from ..fitness.router import router as fitness_router
from ..mindfulness.router import router as mindfulness_router
from ..disease_management.router import router as disease_router
from ..teleconsultation.router import router as teleconsult_router
from ..education.router import router as education_router

app = FastAPI(
    title="ArogyaMitr API",
    description=(
        "REST API for ArogyaMitr Holistic Health Platform.\n"
        "OAuth social login using Google/Apple is stubbed: submit {provider: google|apple, token: any} to /auth/login/social.\n"
        "Use the /auth endpoints for all authentication and registration flows."
    ),
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)

# Register all domain routers
app.include_router(wellness_router)
app.include_router(nutrition_router)
app.include_router(fitness_router)
app.include_router(mindfulness_router)
app.include_router(disease_router)
app.include_router(teleconsult_router)
app.include_router(education_router)

@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint for ArogyaMitr backend."""
    return {"message": "Healthy"}
