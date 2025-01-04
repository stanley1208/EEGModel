import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np

# 1. Load and preprocess the data
file_path = "combined_output.csv"
data = pd.read_csv(file_path)

X = data.drop(columns=['time']).values
y = np.random.choice([0, 1], size=len(X))  # Replace with actual labels

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into train-test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 2. Train XGBoost model with GPU
clf = xgb.XGBClassifier(
    n_estimators=50,
    max_depth=10,
    tree_method="gpu_hist",  # Use GPU acceleration
    random_state=42,
    use_label_encoder=False
)
clf.fit(X_train, y_train)

# 3. Make predictions
y_pred = clf.predict(X_test)

# 4. Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification report:\n", classification_report(y_test, y_pred))
