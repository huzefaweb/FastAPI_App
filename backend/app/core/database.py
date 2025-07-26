from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from typing import Any, Optional

client: Optional[AsyncIOMotorClient[Any]] = None
db = None

async def connect_db():
    global client, db
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    # If you want a named DB, use client["auth_db"] or client.get_default_database()
    db = client[settings.DB_NAME]

async def close_db():
    global client
    if client is not None:
        client.close()
        client = None
