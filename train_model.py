import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

# === Replace this section with loading your real dataset ===
# Example: dataset must have these columns plus target 'BPStage' (0:NORMAL,1:Stage1,2:Stage2,3:Crisis)
# If you have a CSV:
# df = pd.read_csv("your_real_data.csv")

# Synthetic dummy data for structure/testing:
n = 500
np.random.seed(42)
df = pd.DataFrame({
    'Gender': np.random.randint(0, 2, size=n),
    'Age': np.random.randint(20, 80, size=n),
    'Patient': np.random.randint(1000, 2000, size=n),
    'Severity': np.random.randint(1, 5, size=n),
    'BreathShortness': np.random.randint(0, 2, size=n),
    'VisualChanges': np.random.randint(0, 2, size=n),
    'NoseBleeding': np.random.randint(0, 2, size=n),
    'Whendiagnosed': np.random.randint(0, 10, size=n),
    'Systolic': np.random.randint(100, 180, size=n),
    'Diastolic': np.random.randint(60, 120, size=n),
    'ControlledDiet': np.random.randint(0, 2, size=n),
})

# Simulate a target (for real use replace with actual labels)
# Simple rule-based target just for example
def make_stage(row):
    if row.Systolic < 120 and row.Diastolic < 80:
        return 0  # NORMAL
    elif row.Systolic < 140:
        return 1  # Stage-1
    elif row.Systolic < 180:
        return 2  # Stage-2
    else:
        return 3  # Crisis

df['BPStage'] = df.apply(make_stage, axis=1)
# === End synthetic data setup ===

# Features and label
X = df.drop(columns=['BPStage'])
y = df['BPStage']

# Train/test split (optional; you can skip if you just want to train full-model)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Optional: evaluate
print("Training accuracy:", model.score(X_train, y_train))
print("Test accuracy:", model.score(X_test, y_test))

# Save model
joblib.dump(model, 'model.pkl')
print("Model saved to model.pkl")
