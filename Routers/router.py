from fastapi import APIRouter, HTTPException
from typing import List
from Schemas.schema import Patient, Doctor, Appointment

router = APIRouter()

# In-memory storage
patients = []
doctors = []
appointments = []

@router.get('/patients', response_model=List[Patient])
def get_patients():
    return patients

@router.get('/patients/{patient_id}', response_model=Patient)
def get_patient(patient_id: int):
    for patient in patients:
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@router.post('/patients', response_model=Patient, status_code=201)
def create_patient(patient: Patient):
    patients.append(patient)
    return patient

@router.get('/doctors', response_model=List[Doctor])
def get_doctors():
    return doctors

@router.post('/appointments', response_model=Appointment, status_code=201)
def create_appointment(appointment: Appointment):
    # Find the first available doctor
    available_doctors = [doctor for doctor in doctors if doctor.is_available]
    if not available_doctors:
        raise HTTPException(status_code=400, detail="No available doctors")
    
    first_available_doctor = available_doctors[0]
    first_available_doctor.is_available = False
    
    appointment.doctor_id = first_available_doctor.id
    
    appointments.append(appointment)
    
    return appointment