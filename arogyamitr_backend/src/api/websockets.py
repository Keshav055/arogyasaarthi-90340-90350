"""
FastAPI WebSocket endpoints for:
- AI Assistant Chatbot: `ws://host/ws/assistant-chat`
- Tele-consultation Session: `ws://host/ws/teleconsult-session/{session_id}`

Both endpoints return dummy data, echo messages, and broadcast accordingly.
Fully documented for OpenAPI and API usage.
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List, Dict
from jose import JWTError, jwt
import os

router = APIRouter()

# --- Utility for token-based user auth in WebSocket (JWT) ---
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "DO_NOT_USE_IN_PROD")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")


def decode_jwt_token(token: str):
    """
    Decode JWT token and return payload.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        return None

# ---- Chatbot WebSocket Manager (multi-client) ----
class ConnectionManager:
    """
    Manages active websocket connections for a route.
    """
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.clients: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user_id: str = None):
        await websocket.accept()
        self.active_connections.append(websocket)
        if user_id:
            self.clients[user_id] = websocket

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        for k, v in list(self.clients.items()):
            if v is websocket:
                del self.clients[k]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

# One instance per usage
assistant_manager = ConnectionManager()
consult_manager = ConnectionManager()


# PUBLIC_INTERFACE
@router.websocket(
    "/ws/assistant-chat",
    name="Assistant Chatbot WebSocket",
)
async def assistant_chatbot_ws(websocket: WebSocket):
    """
    WebSocket endpoint for real-time interaction with the AI assistant chatbot.

    Usage:
    - Connect with `ws://host/ws/assistant-chat`.
    - Optionally, provide a JWT Bearer token as query param `token` for user context:
      `ws://host/ws/assistant-chat?token=<JWT>`
    - Send chat messages as text frames.
    - Receive chatbot and echo responses as text.

    Stub: This endpoint simply echos your messages, simulates bot replies.
    """
    token = websocket.query_params.get("token")
    user_id = None
    if token:
        payload = decode_jwt_token(token)
        if payload:
            user_id = str(payload.get("sub"))
    await assistant_manager.connect(websocket, user_id)

    try:
        while True:
            in_text = await websocket.receive_text()
            # Echo input and always send dummy bot reply
            await assistant_manager.send_personal_message(f"User: {in_text}", websocket)
            # FAKE BOT LOGIC
            await assistant_manager.send_personal_message(
                "ArogyaMitrBot: (stub reply) How may I assist you today? — [Your question: '{}']".format(in_text),
                websocket
            )
    except WebSocketDisconnect:
        assistant_manager.disconnect(websocket)


# PUBLIC_INTERFACE
@router.websocket(
    "/ws/teleconsult-session/{session_id}",
    name="Tele-consultation WebSocket",
)
async def teleconsult_session_ws(websocket: WebSocket, session_id: str):
    """
    WebSocket endpoint for live tele-consultation (doctor-patient chat/calls).

    Usage:
    - Connect as: `ws://host/ws/teleconsult-session/{session_id}?token=<JWT>`
    - Send/receive text chat messages.
    
    Auth:
    - Requires valid JWT for doctor/user role (pass as query param `token`).
    - This is a mock/stub; no user check is done.
    """
    token = websocket.query_params.get("token")
    user_id = None
    if token:
        payload = decode_jwt_token(token)
        if payload:
            user_id = str(payload.get("sub"))

    await consult_manager.connect(websocket, user_id)
    await consult_manager.send_personal_message(
        f"Welcome to teleconsult session {session_id}. (stub; user_id={user_id})", websocket
    )
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast message to all connected users in the session
            await consult_manager.broadcast(f"[session {session_id}] {user_id or 'user'}: {data}")
    except WebSocketDisconnect:
        consult_manager.disconnect(websocket)
