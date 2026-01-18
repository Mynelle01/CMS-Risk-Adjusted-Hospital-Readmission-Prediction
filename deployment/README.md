# Model Deployment (FastAPI)

## How to Run Locally

1. Clone the repository
    ```bash
    git clone https://github.com/Mynelle01/CMS-Risk-Adjusted-Hospital-Readmission-Prediction.git
    cd CMS-Risk-Adjusted-Hospital-Readmission-Prediction

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate
   
3. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Start the FastAPI application
   ```bash
   cd deployment
   uvicorn app:app

5. Open the API documentation
   Open your browser and go to:
   ```arduino
   http://127.0.0.1:8000/docs

6. Example request
   ```json
   {"features": {
    "time_in_hospital": 9,
    "num_lab_procedures": 62,
    "num_procedures": 0,
    "num_medications": 7,
    "number_outpatient": 0,
    "number_emergency": 1,
    "number_inpatient": 4,
    "number_diagnoses": 4,
    "Diabetes": 0,
    "Heart Disease": 0,
    "Hypertension": 0,
    "Kidney Disease": 0,
    "Other": 1,
    "Respiratory Disease": 0,
    "comorbidity_count": 1,
    "is_emergency_admission": 1,
    "is_elective_admission": 0,
    "is_transfer_in": 0,
    "from_community": 1,
    "admission_source_other": 0,
    "discharged_home": 1,
    "discharged_to_facility": 0,
    "discharged_hospice_or_expired": 0,
    "num_diabetes_meds": 0,
    "on_insulin": 0}
    }

7. Example response
   ```json
   {
    "readmission_probability": 0.42,
    "high_risk": true
   }

## Notes
- Raw datasets are intentionally excluded from version control.
- Feature alignment during inference is enforced using `training_feature_names.json`.
- The API loads a trained GradientBoosting model for inference only.
