# backend/api/index.py
from app.main import app as fastapi_app
from mangum import Mangum

# Mangum wraps your FastAPI app into a lambda‐style handler
handler = Mangum(fastapi_app)
