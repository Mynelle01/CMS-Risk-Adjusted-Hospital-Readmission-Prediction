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
**Predictive performance:**
    - Lower thresholds dramatically improve recall across all models, especially Logistic Regression and Random Forest with >98% recall.
    
    - Precision increases as thresholds rise, but at the cost of missing high-risk patients.
    
    - GradientBoosting with 0.2 threshold resulted to **90% of readmissions** with visible improvement on **precision of 0.125%** suggestiong a more selective risk ranking while still maintaining strong sensitivity. This may be appropriate when hospitals want **high recall with slightly better precision trade-offs.**
    
**Key drivers of readmission:**

    - Prior utilization (inpatient, emergency visits)
    
    - Insulin usage and diabetes medication patterns
    
    - Comorbidity burden and discharge disposition
    
**Interpretability:**

    - SHAP analysis highlighted clinically meaningful risk and protective factors.
    
    - Negative SHAP values identified features associated with reduced readmission risk.
    
**Fairness:**

    - Results are inconclusive due to sparse positive outcomes in several subgroups. 
    
    - A comprehensive fairness assessment should rely on multiple metrics rather than disparate impact alone.
***********************************************************************************
## Author Information

Marinelle Ignacio

Machine Learning & Artificial Intelligence Practitioner

📍 Philippines

Focus: Applied ML, healthcare analytics, model interpretability, fairness

Interests: Predictive modeling, risk adjustment, real-world AI deployment

📫 Feel free to connect via GitHub or LinkedIn
