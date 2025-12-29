from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, doctors, appointments

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Doctor Appointment API", version="1.0.0")

# Include routers
app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Doctor Appointment API"}

