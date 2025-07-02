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

# WebSocket endpoints
from .websockets import router as websocket_router

openapi_tags = [
    {"name": "Health", "description": "Health check and service state endpoints."},
    {"name": "Authentication", "description": "User login/signup and social login APIs"},
    {"name": "Users", "description": "Profile/view/update/delete user profile"},
    {"name": "Wellness", "description": "Wellness Path picks and dashboard tips"},
    {"name": "Nutrition & Diet", "description": "Meal plans, food tracker"},
    {"name": "Fitness", "description": "Fitness activities and goals"},
    {"name": "Mindfulness", "description": "Meditation, Pranayama, mood/journal"},
    {"name": "Disease Management", "description": "Vitals dashboard, logs"},
    {"name": "Teleconsultation", "description": "Appointments, doctors, e-prescription"},
    {"name": "Education Hub", "description": "Articles, videos, infographics"},
    {"name": "WebSocket", "description": (
        "WebSocket (real-time) endpoints: \n"
        "- `/ws/assistant-chat`: AI assistant chatbot socket\n"
        "- `/ws/teleconsult-session/{session_id}`: Doctor-patient consult session socket\n"
        "\n"
        "See the `/websocket-usage` route for instructions and docs."
    )},
]

app = FastAPI(
    title="ArogyaMitr API",
    description=(
        "REST API & WebSockets for ArogyaMitr Holistic Health Platform.\n"
        "OAuth social login using Google/Apple is stubbed: submit {provider: google|apple, token: any} to /auth/login/social.\n"
        "Use the /auth endpoints for all authentication and registration flows.\n"
        "See `/websocket-usage` for WebSocket connection examples."
    ),
    version="0.1.0",
    openapi_tags=openapi_tags,
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

# Register WebSocket API router
app.include_router(websocket_router)

@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint for ArogyaMitr backend."""
    return {"message": "Healthy"}

@app.get("/websocket-usage", tags=["WebSocket"], summary="WebSocket API Usage Guide")
def websocket_usage():
    """
    Realtime WebSocket Usage Guide for API clients.  
    **Endpoints:**
    - `/ws/assistant-chat`: AI chatbot (user agent); Echo demo, optionally pass ?token=
    - `/ws/teleconsult-session/{session_id}`: Consult chat (doctor/patient room); pass ?token=
    
    **Protocol:**
    - Text-frame based chat (send/receive plain text)
    - Pass JWT (from login) as `?token=...` in the URL to associate identity
    - See OpenAPI endpoint docs for connection details.
    """
    return {
        "endpoints": [
            {"path": "/ws/assistant-chat", "desc": "AI assistant chatbot (user) socket"},
            {"path": "/ws/teleconsult-session/{session_id}", "desc": "Tele-consult session socket"}
        ],
        "how_to_connect": [
            "Use plain WebSocket connection.",
            "Send/receive text frames.",
            "Pass login JWT as query param `?token=...` for identity."
        ],
        "notes": "Bots and teleconsult sessions are stubbed for now. See OpenAPI for parameters."
    }
