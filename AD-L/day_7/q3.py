import os
from joblib import effective_n_jobs
import pandas as pd 
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import numpy as np

N_ESTIMATORS = 100
MAX_DEPTH = 3

df = pd.read_csv('data.csv')
df.drop("customerID", axis=1, inplace=True)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.fillna({col: df['TotalCharges'].median() for col in df.columns if df[col].dtype == "object"}, inplace=True)
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
df = pd.get_dummies(df, drop_first=True)

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

model = RandomForestClassifier(random_state=42, n_jobs=-1)

print("Requested jobs:", model.n_jobs)
print("Effective jobs:", effective_n_jobs(model.n_jobs))
print("Total CPU cores:", os.cpu_count())


param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 3, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

fold_num = 1
cv_scores = []

for train_idx, test_idx in kfold.split(X):
    X_train_fold, X_test_fold = X.iloc[train_idx], X.iloc[test_idx]
    y_train_fold, y_test_fold = y.iloc[train_idx], y.iloc[test_idx]
    
    grid_search.fit(X_train_fold, y_train_fold)
    
    best_model = grid_search.best_estimator_
    
    y_pred_fold = best_model.predict(X_test_fold)
    score = best_model.score(X_test_fold, y_test_fold)
    cv_scores.append(score)
        
    cm = confusion_matrix(y_test_fold, y_pred_fold)
    print(f"\nFold {fold_num} - Accuracy: {score:.2f}")
    print(f"Confusion Matrix:\n{cm}")
    
    fold_num += 1

print(f"\nMean CV Accuracy: {np.mean(cv_scores):.2f} -> ({np.std(cv_scores):.2f})")
