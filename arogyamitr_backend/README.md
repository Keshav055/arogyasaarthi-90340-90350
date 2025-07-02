# Project Repository

This is the initial README file for the project.

---

## 🧪 Testing: Running Automated Tests

The backend uses **pytest** (plus FastAPI's test client and `websockets`) for automated API and WebSocket testing.

### To run all tests:

From the `arogyamitr_backend/` project root, run:

```sh
pytest tests/
```

- All API and WebSocket endpoint examples are in `tests/test_api_examples.py`.
- Add new test modules under `tests/` when implementing new endpoints or features.

### Writing New Tests

1. Create new files in the `tests/` directory (names must start with `test_`).
2. Use `fastapi.testclient.TestClient` to test standard endpoints.
3. Use `starlette.testclient`'s `.websocket_connect()` for WebSocket tests.

Example structure for an API test:
```python
def test_some_endpoint():
    resp = client.get("/some-endpoint")
    assert resp.status_code == 200
```

See more inline in `tests/test_api_examples.py`.

---
