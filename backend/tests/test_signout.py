import uuid
import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from asgi_lifespan import LifespanManager
from app.main import app

@pytest.mark.asyncio
async def test_signout_success():
    # Sign up and log in to obtain tokens
    random_email = f"alice_{uuid.uuid4().hex}@example.com"
    password = "StrongP@ssw0rd"
    signup_payload = {
        "first_name": "Alice",
        "last_name":  "Doe",
        "email":      random_email,
        "phone":      "+971501234567",
        "address":    "Dubai, UAE",
        "password":   password
    }
    transport = ASGITransport(app)
    async with LifespanManager(app):
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            signup_resp = await ac.post("/auth/signup", json=signup_payload)
            assert signup_resp.status_code == 201

            login_resp = await ac.post("/auth/login", json={
                "email": random_email,
                "password": password
            })
            assert login_resp.status_code == 200
            tokens = login_resp.json()
            access_token = tokens["access_token"]

            signout_resp = await ac.post(
                "/auth/signout",
                headers={"Authorization": f"Bearer {access_token}"}
            )

    assert signout_resp.status_code == 204
