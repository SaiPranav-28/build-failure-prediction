import joblib
import pandas as pd

# Load trained Random Forest model
model = joblib.load("model/random_forest_model.joblib")

# Example information for a new build
new_build = pd.DataFrame([{
    "previous_build_result": 1,
    "previous_build_duration": 190,
    "recent_failures": 2,
    "files_changed": 10,
    "lines_added": 180,
    "lines_deleted": 60,
    "historical_failure_ratio": 0.28
}])

# Predict failure probability
failure_probability = model.predict_proba(new_build)[0][1]

# Convert probability to percentage
failure_percentage = failure_probability * 100

# Determine risk level
if failure_percentage >= 70:
    risk = "HIGH"
elif failure_percentage >= 40:
    risk = "MEDIUM"
else:
    risk = "LOW"

print("======================================")
print("Build Failure Prediction")
print("======================================")
print(f"Failure Probability: {failure_percentage:.2f}%")
print(f"Risk Level: {risk}")
print("======================================")
