import os
from joblib import effective_n_jobs
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

N_ESTIMATORS = 500
MAX_DEPTH = 3

df = pd.read_csv("data.csv")

df.drop("customerID", axis=1, inplace=True)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
# df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

df.fillna(
    {
        col: df["TotalCharges"].median()
        for col in df.columns
        if df[col].dtype == "object"
    },
    inplace=True,
)

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

df = pd.get_dummies(df, drop_first=True)

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=N_ESTIMATORS, criterion="gini", max_depth=MAX_DEPTH, random_state=42,n_jobs=-1
)

print("Requested jobs:", model.n_jobs)
print("Effective jobs:", effective_n_jobs(model.n_jobs))
print("Total CPU cores:", os.cpu_count())
    
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = model.score(X_test, y_test)

print(f"\nOverall Accuracy: {accuracy:.2f}")

print("Confusion Matrix:")
print(pd.crosstab(y_test, y_pred, rownames=["Actual"], colnames=["Predicted"]))

print("Classification Report:")
print(classification_report(y_test, y_pred))


def save_results():
    with open(f"results_EST_{N_ESTIMATORS}_D_{MAX_DEPTH}.txt", "w") as f:
        f.write(f"Random Forest Classifier Results\n")
        f.write(f"Parameters: n_estimators={N_ESTIMATORS}, max_depth={MAX_DEPTH}\n\n")
        f.write(f"Overall Accuracy: {accuracy:.2f}\n\n")
        f.write("Confusion Matrix:\n")
        f.write(
            pd.crosstab(
                y_test, y_pred, rownames=["Actual"], colnames=["Predicted"]
            ).to_string()
        )
        f.write("\n\nClassification Report:\n")
        f.write(classification_report(y_test, y_pred))
        
save_results()


