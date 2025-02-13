import pandas as pd
import joblib
import os
import json

def predict_furnace_temps(width, thickness, gsm_a, tph, model_folder='furnace_model'):
    rf_model = joblib.load(os.path.join(model_folder, 'rf_model.joblib'))
    scaler = joblib.load(os.path.join(model_folder, 'scaler.joblib'))
    with open(os.path.join(model_folder, 'targets.json'), 'r') as f:
        targets = json.load(f)
    
    input_data = pd.DataFrame([[width, thickness, gsm_a, tph]], columns=['Width', 'Thickness', 'GSM-A', 'TPH'])
    input_scaled = scaler.transform(input_data)
    predictions = rf_model.predict(input_scaled)
    
    result = {}
    for target, pred in zip(targets, predictions[0]):
        result[target] = float(pred)
    
    return result