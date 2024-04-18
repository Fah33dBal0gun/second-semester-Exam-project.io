from pydantic import BaseModel
from typing import Optional, List

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: int

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: int
    is_available: Optional[bool] = True

class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: str