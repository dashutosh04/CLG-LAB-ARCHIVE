import json
import matplotlib.pyplot as plt 
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

QUES = 3

df = pd.read_csv("student-por.csv")
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

features = ['studytime', 'absences', 'failures', 'G1', 'G2']
target = 'G3'

X = df[features]
y = df[target]

os.makedirs(f"outputs_{QUES}", exist_ok=True)

config_file = "config.json"


with open(config_file, 'r') as f:
    config = json.load(f)


TEST_SIZE = config.get("test_size", 0.2)
TYPE = config.get("type", 1)
RANDOM_STATE = config.get("random_state", 42)
MAX_DEPTH = config.get("max_depth", 4)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y if TYPE == 1 and len(set(y)) > 1 else None)
clf = DecisionTreeClassifier(random_state=RANDOM_STATE, max_depth=MAX_DEPTH)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

df['pass_fail'] = df['G3'].apply(lambda x: 1 if x >= 10 else 0)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

print("Classification Report:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print("rows: actual, columns: predicted")
print("                          Fail  Pass")
for i, species in enumerate(["Fail", "Pass"]):
    print(f"{species:12} {cm[i][0]:7} {cm[i][1]:11}")

print("Manual precision, recall, F1-score calculation:")
for i, species in enumerate(["Fail", "Pass"]):
    TP = cm[i][i]
    FP = sum(cm[:, i]) - TP
    FN = sum(cm[i, :]) - TP
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    print(f"{species}: Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1:.4f}")

with open(os.path.join(f"outputs_{QUES}", f"confusion_matrix_type_{TYPE}_TS_{TEST_SIZE}_RS_{RANDOM_STATE}_MD_{MAX_DEPTH}.txt"), 'w') as f:
    f.write("Confusion Matrix:\n")
    f.write("rows: actual, columns: predicted\n")
    f.write("                          Fail  Pass\n")
    for i, species in enumerate(["Fail", "Pass"]):
        f.write(f"{species:12} {cm[i][0]:7} {cm[i][1]:11}\n")
    f.write("\nManual precision, recall, F1-score calculation:\n")
    for i, species in enumerate(["Fail", "Pass"]):
        TP = cm[i][i]
        FP = sum(cm[:, i]) - TP
        FN = sum(cm[i, :]) - TP
        precision = TP / (TP + FP) if (TP + FP) != 0 else 0
        recall = TP / (TP + FN) if (TP + FN) != 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
        f.write(f"{species}: Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1:.4f}\n")

plt.figure(figsize=(60, 40))
plot_tree(clf, filled=True, feature_names=df.columns[:-1])
plt.title(f"Decision Tree for Student Grades - {TYPE}, Test Size: {TEST_SIZE}, Random State: {RANDOM_STATE}, Max Depth: {MAX_DEPTH}")

plt.savefig(os.path.join(f"outputs_{QUES}", f"decision_tree_type_{TYPE}_TS_{TEST_SIZE}_RS_{RANDOM_STATE}_MD_{MAX_DEPTH}.png"))
plt.show()
