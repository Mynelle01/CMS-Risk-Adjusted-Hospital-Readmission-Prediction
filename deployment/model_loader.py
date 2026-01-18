import joblib
import json

MODEL_PATH = "../models/GradientBoosting_final.pkl"
FEATURES_PATH = "../models/training_feature_names.json"

def load_model():
    model = joblib.load(MODEL_PATH)
    with open(FEATURES_PATH, "r") as f:
        feature_names = json.load(f)
    return model, feature_names