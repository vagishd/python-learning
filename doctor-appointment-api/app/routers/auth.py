from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserRegister, UserLogin, Token, UserResponse, ForgotPassword
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    user = AuthService.register_user(db, user_data)
    return user


@router.post("/login", response_model=Token)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    token = AuthService.login_user(db, login_data)
    return token


@router.post("/forgot-password")
def forgot_password(forgot_data: ForgotPassword, db: Session = Depends(get_db)):
    result = AuthService.forgot_password(db, forgot_data.email)
    return result

