from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User schemas
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    role: str
    name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    role: str
    name: str
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class ForgotPassword(BaseModel):
    email: EmailStr


class AvailabilityCreate(BaseModel):
    start_time: datetime
    end_time: datetime

class AvailabilityResponse(BaseModel):
    id: int
    doctor_id: int
    start_time: datetime
    end_time: datetime
    
    class Config:
        from_attributes = True


class AppointmentCreate(BaseModel):
    doctor_id: int
    appointment_time: datetime

class AppointmentResponse(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    appointment_time: datetime
    status: str
    
    class Config:
        from_attributes = True


class DoctorResponse(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True

