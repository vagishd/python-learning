from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import AppointmentCreate, AppointmentResponse
from app.services.appointment_service import AppointmentService
from app.dependencies import get_current_patient
from typing import List

router = APIRouter(prefix="/appointments", tags=["Appointments"])

# Book appointment (only for patients)
@router.post("/book", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def book_appointment(
    appointment_data: AppointmentCreate,
    db: Session = Depends(get_db),
    current_patient: User = Depends(get_current_patient)
):
    appointment = AppointmentService.book_appointment(db, current_patient.id, appointment_data)
    return appointment

# Cancel appointment (only for patients)
@router.post("/{appointment_id}/cancel", response_model=AppointmentResponse)
def cancel_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_patient: User = Depends(get_current_patient)
):
    appointment = AppointmentService.cancel_appointment(db, appointment_id, current_patient.id)
    return appointment

