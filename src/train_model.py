import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os

# Load historical build data
data = pd.read_csv("data/build_history.csv")

features = [
    "previous_build_result",
    "previous_build_duration",
    "recent_failures",
    "files_changed",
    "lines_added",
    "lines_deleted",
    "historical_failure_ratio"
]

X = data[features]
y = data["build_failed"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("======================================")
print("Random Forest Model Training")
print("======================================")
print(f"Accuracy : {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall   : {recall:.2f}")
print(f"F1 Score : {f1:.2f}")

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/random_forest_model.joblib")

print("======================================")
print("Model saved successfully!")
print("Location: model/random_forest_model.joblib")
print("======================================")
