from sqlalchemy.orm import Session
from app.models import User, Availability, Appointment
from app.schemas import AvailabilityCreate, AppointmentCreate
from fastapi import HTTPException, status
from datetime import datetime

# Service for appointment operations
class AppointmentService:
    
    @staticmethod
    def set_availability(db: Session, doctor_id: int, availability_data: AvailabilityCreate):
        # Check if doctor exists
        from app.models import UserRole
        doctor = db.query(User).filter(User.id == doctor_id).first()
        if not doctor or doctor.role != UserRole.DOCTOR:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )
        
        # Validate time range
        if availability_data.start_time >= availability_data.end_time:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Start time must be before end time"
            )
        
        # Create availability
        new_availability = Availability(
            doctor_id=doctor_id,
            start_time=availability_data.start_time,
            end_time=availability_data.end_time
        )
        
        db.add(new_availability)
        db.commit()
        db.refresh(new_availability)
        
        return new_availability
    
    @staticmethod
    def get_doctor_availability(db: Session, doctor_id: int):
        # Check if doctor exists
        from app.models import UserRole
        doctor = db.query(User).filter(User.id == doctor_id).first()
        if not doctor or doctor.role != UserRole.DOCTOR:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )
        
        # Get all availabilities for this doctor
        availabilities = db.query(Availability).filter(Availability.doctor_id == doctor_id).all()
        
        return availabilities
    
    @staticmethod
    def get_doctors(db: Session):
        # Get all users with role Doctor
        from app.models import UserRole
        doctors = db.query(User).filter(User.role == UserRole.DOCTOR).all()
        return doctors
    
    @staticmethod
    def book_appointment(db: Session, patient_id: int, appointment_data: AppointmentCreate):
        # Check if doctor exists
        from app.models import UserRole
        doctor = db.query(User).filter(User.id == appointment_data.doctor_id).first()
        if not doctor or doctor.role != UserRole.DOCTOR:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )
        
        # Check if appointment time is in the future
        if appointment_data.appointment_time <= datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Appointment time must be in the future"
            )
        
        # Check if doctor has availability at this time
        availabilities = db.query(Availability).filter(
            Availability.doctor_id == appointment_data.doctor_id,
            Availability.start_time <= appointment_data.appointment_time,
            Availability.end_time >= appointment_data.appointment_time
        ).first()
        
        if not availabilities:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Doctor is not available at this time"
            )
        
        # Check for double booking (doctor already has appointment at this time)
        existing_appointment = db.query(Appointment).filter(
            Appointment.doctor_id == appointment_data.doctor_id,
            Appointment.appointment_time == appointment_data.appointment_time,
            Appointment.status == "scheduled"
        ).first()
        
        if existing_appointment:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Doctor already has an appointment at this time"
            )
        
        # Create appointment
        new_appointment = Appointment(
            doctor_id=appointment_data.doctor_id,
            patient_id=patient_id,
            appointment_time=appointment_data.appointment_time,
            status="scheduled"
        )
        
        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)
        
        return new_appointment
    
    @staticmethod
    def get_doctor_appointments(db: Session, doctor_id: int):
        # Get all appointments for this doctor
        appointments = db.query(Appointment).filter(
            Appointment.doctor_id == doctor_id,
            Appointment.status == "scheduled"
        ).all()
        
        return appointments
    
    @staticmethod
    def cancel_appointment(db: Session, appointment_id: int, patient_id: int):
        # Get appointment
        appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
        
        if not appointment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Appointment not found"
            )
        
        # Check if patient owns this appointment
        if appointment.patient_id != patient_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only cancel your own appointments"
            )
        
        # Cancel appointment
        appointment.status = "cancelled"
        db.commit()
        db.refresh(appointment)
        
        return appointment

