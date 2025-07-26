from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId
from app.schemas.user import UserCreate, UserLogin, Token
from app.auth.hash import hash_password, verify_password
from app.core.security import create_access_token, create_refresh_token, verify_token, oauth2_scheme
from app.core import database

router = APIRouter()

@router.post("/signup", response_model=Token, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate):
    # Check for existing email
    if await database.db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    # Hash the password
    hashed = hash_password(user.password)
    user_dict = user.model_dump(exclude={"password"})
    user_dict["hashed_password"] = hashed
    # Insert new user
    result = await database.db.users.insert_one(user_dict)
    user_id = str(result.inserted_id)
    # Create tokens
    access = create_access_token({"user_id": user_id})
    refresh = create_refresh_token({"user_id": user_id})
    # Store refresh token
    await database.db.users.update_one(
        {"_id": result.inserted_id}, {"$set": {"refresh_token": refresh}}
    )
    return {"access_token": access, "refresh_token": refresh}

@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    # Retrieve user from DB
    db_user = await database.db.users.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    user_id = str(db_user["_id"])
    # Create tokens
    access = create_access_token({"user_id": user_id})
    refresh = create_refresh_token({"user_id": user_id})
    # Update stored refresh token
    await database.db.users.update_one(
        {"_id": db_user["_id"]}, {"$set": {"refresh_token": refresh}}
    )
    return {"access_token": access, "refresh_token": refresh}

@router.post("/signout", status_code=status.HTTP_204_NO_CONTENT)
async def signout(token: str = Depends(oauth2_scheme)):
    # Verify access token and clear refresh token
    payload = verify_token(token, token_type="access")
    user_obj_id = ObjectId(payload.user_id)
    await database.db.users.update_one(
        {"_id": user_obj_id}, {"$set": {"refresh_token": None}}
    )
    return
