from fastapi import APIRouter, Depends, HTTPException
from app.models.user import create_user, find_user_by_email
from app.schemas.user import UserCreate, UserLogin
from app.utils.auth import create_access_token

router = APIRouter()

@router.post("/signup")
def signup(user: UserCreate):
    user_id = create_user(user.name, user.email, user.password)
    token = create_access_token({"sub": user.email})
    return {"token": token}

@router.post("/login")
def login(user: UserLogin):
    db_user = find_user_by_email(user.email)
    if not db_user or db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user["email"]})
    return {"token": token}