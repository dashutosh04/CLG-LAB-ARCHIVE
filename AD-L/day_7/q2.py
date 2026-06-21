import os
from joblib import effective_n_jobs
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
import numpy as np

N_ESTIMATORS = 100
MAX_DEPTH = 3


df = pd.read_csv('data.csv')

df.drop("customerID", axis=1, inplace=True)

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
#df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

df.fillna({col:df['TotalCharges'].median() for col in df.columns if df[col].dtype == "object"}, inplace=True)

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

df = pd.get_dummies(df, drop_first=True)

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42,stratify=y)

model = RandomForestClassifier(n_estimators=N_ESTIMATORS,criterion='gini', max_depth=MAX_DEPTH, random_state=42,n_jobs=-1)

print("Requested jobs:", model.n_jobs)
print("Effective jobs:", effective_n_jobs(model.n_jobs))
print("Total CPU cores:", os.cpu_count())
    
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = model.score(X_test, y_test)

print(f"Overall Accuracy: {accuracy:.2f}")

print("Confustion Matrix:")
print(pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))

print("Classification Report:")
print(classification_report(y_test, y_pred))


kfold = KFold(n_splits=5, shuffle=True, random_state=42)

fold_num = 1
cv_scores = []

for train_idx, test_idx in kfold.split(X):
    X_train_fold, X_test_fold = X.iloc[train_idx], X.iloc[test_idx]
    y_train_fold, y_test_fold = y.iloc[train_idx], y.iloc[test_idx]
    
    model_fold = RandomForestClassifier(n_estimators=N_ESTIMATORS, criterion='gini', max_depth=MAX_DEPTH, random_state=42)
    model_fold.fit(X_train_fold, y_train_fold)
    
    y_pred_fold = model_fold.predict(X_test_fold)
    score = model_fold.score(X_test_fold, y_test_fold)
    cv_scores.append(score)
    
    cm = confusion_matrix(y_test_fold, y_pred_fold)
    print(f"\nFold {fold_num} - Accuracy: {score:.2f}")
    print(f"Confusion Matrix:\n{cm}")
    
    fold_num += 1

print(f"\nMean CV Accuracy: {np.mean(cv_scores):.2f} -> ({np.std(cv_scores):.2f})")