from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import AvailabilityCreate, AvailabilityResponse, AppointmentResponse, DoctorResponse
from app.services.appointment_service import AppointmentService
from app.dependencies import get_current_doctor, get_current_user
from typing import List

router = APIRouter(prefix="/doctors", tags=["Doctors"])

# Get all doctors (available to all authenticated users)
@router.get("/all", response_model=List[DoctorResponse])
def get_doctors(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    doctors = AppointmentService.get_doctors(db)
    return doctors

# Get doctor availability
@router.get("/{doctor_id}/availability", response_model=List[AvailabilityResponse])
def get_doctor_availability(doctor_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    availabilities = AppointmentService.get_doctor_availability(db, doctor_id)
    return availabilities

# Set availability (only for doctors)
@router.post("/availability", response_model=AvailabilityResponse)
def set_availability(
    availability_data: AvailabilityCreate,
    db: Session = Depends(get_db),
    current_doctor: User = Depends(get_current_doctor)
):
    availability = AppointmentService.set_availability(db, current_doctor.id, availability_data)
    return availability

# Get doctor's upcoming appointments
@router.get("/appointments", response_model=List[AppointmentResponse])
def get_my_appointments(
    db: Session = Depends(get_db),
    current_doctor: User = Depends(get_current_doctor)
):
    appointments = AppointmentService.get_doctor_appointments(db, current_doctor.id)
    return appointments

