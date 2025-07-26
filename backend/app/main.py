from fastapi import FastAPI
from app.routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.protected import router as protected_router
from app.core.database import connect_db, close_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await close_db()

app = FastAPI(
    title="Auth App v1",
    description="FastAPI service with JWT-powered auth (access + refresh tokens)",
    version="1.0.0",
    lifespan=lifespan,
)

# Allow your frontend origin
origins = [
    "http://localhost:3000",
    # you can add other origins here (e.g. if deployed)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],              # permit GET, POST, OPTIONS, etc.
    allow_headers=["*"],              # permit all headers
)

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Auth App v1 is up and running"}

# Mount our routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(protected_router, tags=["Protected"])
