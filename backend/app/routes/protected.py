from fastapi import APIRouter, Depends
from app.core.security import oauth2_scheme, verify_token
from app.schemas.user import TokenData

router = APIRouter()

@router.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    # Only valid access tokens reach here
    payload: TokenData = verify_token(token, token_type="access")
    return {"message": f"Hello, user {payload.user_id}"}
