from fastapi import FastAPI
from pydantic import BaseModel
from app.services.pipeline import run_pipeline

app = FastAPI()

# Request schema
class PatientRecord(BaseModel):
    text: str

# Health check
@app.get("/")
def root():
    return {"message": "EHR De-Identification API is running"}

# MVP endpoint
@app.post("/deidentify")
def deidentify(record: PatientRecord):
    result = run_pipeline(record.text)

    return {
        "original_text": record.text,
        "deidentified_text": result
    }