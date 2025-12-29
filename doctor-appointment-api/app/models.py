from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from datetime import datetime


class UserRole(enum.Enum):
    DOCTOR = "Doctor"
    PATIENT = "Patient"

# User model
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    availabilities = relationship("Availability", back_populates="doctor")
    appointments_as_doctor = relationship("Appointment", foreign_keys="[Appointment.doctor_id]", back_populates="doctor")
    appointments_as_patient = relationship("Appointment", foreign_keys="[Appointment.patient_id]", back_populates="patient")

# Availability model
class Availability(Base):
    __tablename__ = "availabilities"
    
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    doctor = relationship("User", back_populates="availabilities")

# Appointment model
class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    status = Column(String, default="scheduled")  # scheduled, cancelled, completed
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    doctor = relationship("User", foreign_keys=[doctor_id], back_populates="appointments_as_doctor")
    patient = relationship("User", foreign_keys=[patient_id], back_populates="appointments_as_patient")

