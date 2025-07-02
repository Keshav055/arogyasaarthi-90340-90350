# ArogyaMitr Backend API Documentation: Endpoint Overview and Usage Examples

## General Information

- **Base URL (Local Dev):** `http://localhost:8000`
- **OpenAPI UI:** `/docs`
- **OpenAPI Spec:** `/openapi.json`
- **Authentication:** JWT Bearer tokens for most endpoints; obtain via `/auth/login`, attach as `Authorization: Bearer <token>`
- **WebSockets:** Real-time API, see `/websocket-usage` for guide.

---

## Health & Info

- `GET /`
  - Health check; returns alive signal

- `GET /websocket-usage`
  - Shows real-time WebSocket endpoint usage and protocol

---

## Authentication

- `POST /auth/signup`
  - Register a new user.
  - Body: `{"email": "...", "password": "...", "name": "..."}`

- `POST /auth/login`
  - Login using email/password (form fields: `username`, `password`)
  - Returns JWT token

- `POST /auth/login/social`
  - Social login (Google/Apple, stub)
  - Body: `{"provider": "google", "token": "anything"}`

- `GET /auth/me`
  - Returns the authenticated user's profile (JWT required)

---

## User Profile

- `GET /users/me`
  - Get current user profile (JWT required)

- `PUT /users/me`
  - Update profile fields (body: name, phone, age, ...)

- `DELETE /users/me`
  - Delete user account

---

## Wellness

- `GET /wellness/tips`
  - List wellness tips (JWT required)

- `POST /wellness/select-path`
  - Select a wellness path (body: user_id, selected_path)

---

## Nutrition & Diet

- `GET /nutrition/plans`
  - List nutrition plans (JWT required)

- `GET /nutrition/meals`
  - List meals with nutrition info

---

## Fitness

- `GET /fitness/activities`
  - List fitness activities

- `GET /fitness/goals`
  - Returns user's fitness goals

---

## Mindfulness

- `GET /mindfulness/meditations`
  - List meditation session logs

- `POST /mindfulness/mood`
  - Post a mood/journal (body: user_id, mood, ...)

---

## Disease Management

- `GET /disease/vitals`
  - List recent vitals (JWT required)

- `POST /disease/log`
  - Add a disease log (body: user_id, condition, ...)

---

## Teleconsultation

- `GET /teleconsult/doctors`
  - List doctors

- `POST /teleconsult/appointments`
  - Book appointment (body: user_id, doctor_id, ...)

---

## Education Hub

- `GET /education/articles`
  - List educational articles

- `GET /education/videos`
  - List educational videos

---

## WebSocket API

- `/ws/assistant-chat`
  - AI assistant chatbot socket (send/receive text; pass JWT with `?token=...`)
- `/ws/teleconsult-session/{session_id}`
  - Doctor-patient room socket

**See `/websocket-usage` route and OpenAPI docs for protocol and usage samples**

---

## Example: Authenticated Request

```
POST /auth/login -> { "access_token": ... }
Authorization: Bearer <access_token>
GET /wellness/tips
```

## Example: WebSocket Connect (Python)

```python
import websockets
async def ws():
    ws_url = "ws://localhost:8000/ws/assistant-chat?token=<JWT>"
    async with websockets.connect(ws_url) as ws:
        await ws.send("Hi bot")
        print(await ws.recv())
        print(await ws.recv())
```

---

## Testing

Run all API tests:  
```
pytest tests/
```

---

**For full schema details and live API tryout, see `/docs` on your running backend (FastAPI OpenAPI UI).**
