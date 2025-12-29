from sqlalchemy.orm import Session
from app.models import User, UserRole
from app.schemas import UserRegister, UserLogin
from app.utils import hash_password, verify_password, create_access_token
from fastapi import HTTPException, status

# Service for authentication operations
class AuthService:
    
    @staticmethod
    def register_user(db: Session, user_data: UserRegister):
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Validate role
        if user_data.role not in ["Doctor", "Patient"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Role must be either 'Doctor' or 'Patient'"
            )
        
        # Hash password
        hashed_password = hash_password(user_data.password)
        
        # Create user
        new_user = User(
            email=user_data.email,
            password_hash=hashed_password,
            role=UserRole.DOCTOR if user_data.role == "Doctor" else UserRole.PATIENT,
            name=user_data.name
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
    
    @staticmethod
    def login_user(db: Session, login_data: UserLogin):
        # Find user by email
        user = db.query(User).filter(User.email == login_data.email).first()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Verify password
        if not verify_password(login_data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Create token
        token_data = {"sub": user.email, "user_id": user.id, "role": user.role.value}
        access_token = create_access_token(token_data)
        
        return {"access_token": access_token, "token_type": "bearer"}
    
    @staticmethod
    def forgot_password(db: Session, email: str):
        # Check if user exists
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            return {"message": "If the email exists, a password reset link has been sent"}
        

        return {"message": "If the email exists, a password reset link has been sent"}

