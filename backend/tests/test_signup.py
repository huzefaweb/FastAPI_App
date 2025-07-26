import uuid
import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from asgi_lifespan import LifespanManager
from app.main import app

@pytest.mark.asyncio
async def test_signup_success():
    # Use a unique email to avoid conflicts
    random_email = f"alice_{uuid.uuid4().hex}@example.com"
    payload = {
        "first_name": "Alice",
        "last_name":  "Doe",
        "email":      random_email,
        "phone":      "+971501234567",
        "address":    "Dubai, UAE",
        "password":   "StrongP@ssw0rd"
    }

    transport = ASGITransport(app)
    async with LifespanManager(app):
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/auth/signup", json=payload)

    assert response.status_code == 201
    data = response.json()
    # New: assert both tokens are returned
    assert "access_token" in data and isinstance(data["access_token"], str)
    assert "refresh_token" in data and isinstance(data["refresh_token"], str)
