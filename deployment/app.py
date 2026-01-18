from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import load_model
from predict import predict_readmission

app = FastAPI(title="30-Day Readmission Predictor")

model, feature_names = load_model()

class PatientInput(BaseModel):
    features: dict

@app.post("/predict")
def predict(input_data: PatientInput):
    return predict_readmission(model, feature_names, input_data)