****************************************************************************
# **CMS-Risk-Adjusted-Hospital-Readmission-Prediction**
Final requirement for my machine learning and artificial intelligence course
*****************************************************************************
## **Project Description**
  This project builds a **machine learning–based risk prediction system** to identify patients at high risk of **hospital readmission within 30 days.**
The goal is to support hospitals in **reducing avoidable readmissions**, improving care quality, and **mitigating CMS financial penalties** through data-driven decision-making.

  The model leverages patient demographics, comorbidities, medication usage, prior utilization, and clinical history to generate actionable risk scores that can be used for targeted post-discharge interventions.
******************************************************************************
## **Problem Statement**
  *"This project mirrors **CMS risk-adjusted readmission modeling** used in U.S. hospital reimbursement, where inaccurate prediction can lead to multi-million-dollar penalties."*
******************************************************************************
## **Dataset Source & Description**
***Source:** UCI Machine Learning Repository. (n.d.). https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008*
***Scope:** Over 100,000 inpatient encounters*
***Key Features:***
  - Demographics (age, gender, race, payer_code)
  - Diagnoses (ICD-9 codes)
  - Comorbidities and chronic conditions
  - Medication usage (diabetes drugs, insulin)
  - Prior utilization (outpatient, emergency, inpatient visits)
***Target Variable:** Readmission status (<30, >30, NO), binarized for prediction*
********************************************************************************
## **Installation Instructions**
**Prerequisites:**
  - Python 3.11.x
  - Virtual environment (recommended)
**Install dependencies** using *capstone_requirements.txt
**How to Run the Code**
  - Activate your virtual environment
  - Run the Jupyter Notebook
  - Click **Run All** to execute all code cells
********************************************************************************
## **Results Summary**

**Predictive performance**
    - Models AUC-ROC resulted to poor discrimination and low Recall, possibly due to dropped columns for minimizing runtime.
    
**Key drivers of readmission**
    - Prior utilization (outpatient, inpatient, emergency visits)
    - Insulin usage and diabetes medication patterns
    - Comorbidity burden and discharge disposition
    
**Interpretability**
    - SHAP analysis highlighted clinically meaningful risk and protective factors.
    - Negative SHAP values identified features associated with reduced readmission risk.
    
**Fairness**
    - Fairness metrics (TPR, FPR, disparate impact) revealed disparities across race, gender, and age groups.
***********************************************************************************
## Author Information

Marinelle Ignacio

Machine Learning & Artificial Intelligence Practitioner

📍 Philippines

Focus: Applied ML, healthcare analytics, model interpretability, fairness

Interests: Predictive modeling, risk adjustment, real-world AI deployment

📫 Feel free to connect via GitHub or LinkedIn
