"""
Minimal backend API and WebSocket test scaffolding for ArogyaMitr.

- Requires FastAPI test client: `pytest`, `httpx`, and `websockets`.
- Each sample test demonstrates a basic usage flow for the critical endpoints and is heavily commented.
- To run: `pytest` from the `arogyamitr_backend` project root.
"""

from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health_check():
    """Test the health check endpoint /."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Healthy" in resp.json()["message"]

def test_signup_and_login_flow(monkeypatch):
    """Test user signup and login, and fetch profile (core auth flow)."""

    # Patch fake_users_db for parallel test isolation
    from src.users import service as user_service
    user_service.fake_users_db.clear()

    # Signup
    signup_payload = {"email": "test@example.com", "password": "pass123", "name": "Test User"}
    r = client.post("/auth/signup", json=signup_payload)
    assert r.status_code == 200
    assert r.json()["email"] == "test@example.com"

    # Login
    response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "pass123",
    })
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # /auth/me
    me = client.get("/auth/me", headers=headers)
    assert me.status_code == 200
    assert me.json()["email"] == "test@example.com"

def test_wellness_tips_authenticated():
    """Test wellness tips API with login."""
    from src.users import service as user_service
    user_service.fake_users_db.clear()

    # Ensure user in DB and get token
    signup_payload = {"email": "tt@example.com", "password": "p", "name": "T T"}
    client.post("/auth/signup", json=signup_payload)
    response = client.post("/auth/login", data={
        "username": "tt@example.com",
        "password": "p"
    })
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    resp = client.get("/wellness/tips", headers=headers)
    assert resp.status_code == 200
    assert type(resp.json()) is list

def test_websocket_assistant_chat():
    """Showcase websocket assistant chat endpoint demo (no assertion, for docs)."""
    # This is not a true async pytest test, just for documentation.
    from starlette.testclient import TestClient as StarletteClient
    sc = StarletteClient(app)
    with sc.websocket_connect("/ws/assistant-chat") as ws:
        ws.send_text("Hello?")
        text1 = ws.receive_text()
        text2 = ws.receive_text()
        assert "User: Hello?" in text1
        assert "ArogyaMitrBot" in text2

# Add more tests for each module as needed: /nutrition/plans, /fitness/activities, etc.

"""
==== Usage Examples for API Consumers ====

# Signup (POST)
/auth/signup
Payload: {"email": "x@y.com", "password": "...", "name": "Name"}
Response: user profile data

# Login (POST form)
/auth/login
Form fields: username, password
Response: {"access_token": "...", "token_type": "bearer"}

# Use the token
Authorization Header: Bearer <access_token> (for all protected endpoints)

# WebSocket Chat Example (Python)
import websockets
async def ws_demo():
    async with websockets.connect("ws://localhost:8000/ws/assistant-chat?token=<JWT>") as ws:
        await ws.send("Hi")
        msg1 = await ws.recv()
        msg2 = await ws.recv()

# Each API route is tagged and described in the OpenAPI UI (see /docs endpoint or openapi.json for details).
"""
