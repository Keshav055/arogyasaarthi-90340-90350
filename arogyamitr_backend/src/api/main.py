from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..auth.router import router as auth_router
from ..users.router import router as users_router

app = FastAPI(
    title="ArogyaMitr API",
    description=(
        "REST API for ArogyaMitr Holistic Health Platform.\n\n"
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

@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint for ArogyaMitr backend."""
    return {"message": "Healthy"}
