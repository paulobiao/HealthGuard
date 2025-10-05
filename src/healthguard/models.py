
from pydantic import BaseModel, Field
from typing import Optional

class Patient(BaseModel):
    patient_id: str
    name: str
    dob: str
    diagnosis: Optional[str] = None

class RecordIn(BaseModel):
    patient: Patient
    notes: str = Field(default="", max_length=2000)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
