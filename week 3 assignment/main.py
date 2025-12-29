from fastapi import FastAPI
from database import engine, Base
from auth import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

