import pandas as pd

def predict_readmission(model, feature_names, input_data):
    # Convert input dict to DataFrame
    df = pd.DataFrame([input_data.features])

    # Force correct feature set and order
    df = df.reindex(columns=feature_names, fill_value=0)

    prob = model.predict_proba(df)[0, 1]

    return {
        "readmission_probability": round(float(prob), 4),
        "high_risk": bool(prob >= 0.30)
    }