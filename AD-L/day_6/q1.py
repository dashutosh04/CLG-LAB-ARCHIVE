import matplotlib.pyplot as plt 
import numpy as np
import json,os
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
os.makedirs("outputs_1", exist_ok=True)

config_file = "config.json"

with open(config_file, 'r') as f:
    config = json.load(f)
    
TEST_SIZE = config.get("test_size")
TYPE = config.get("type")
RANDOM_STATE = config.get("random_state", 42)

iris = load_iris()
x,y = iris.data, iris.target


if TYPE == 1:
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE, random_state=RANDOM_STATE,stratify=y)
    clf = DecisionTreeClassifier(random_state=RANDOM_STATE)
elif TYPE == 2:
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)
    clf = DecisionTreeClassifier(random_state=RANDOM_STATE)
else:
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE)
    clf = DecisionTreeClassifier()


clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}%")

print("Classification Report:")
print(classification_report(y_test, y_pred,target_names=iris.target_names))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print("rows: actual, columns: predicted")
print("                          Setosa  Versicolor  Virginica")
for i, species in enumerate(iris.target_names):
    print(f"{species:12} {cm[i][0]:7} {cm[i][1]:11} {cm[i][2]:10}")
    
    
print("Manual precision, recall, F1-score calculation:")

precision = recall = f1_score = 0

for i, species in enumerate(iris.target_names):
    TP = cm[i][i]
    FP = sum(cm[:,i]) - TP
    FN = sum(cm[i,:]) - TP
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    print(f"{species}: Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1_score:.4f}")    

with open(os.path.join("outputs_1", f"confusion_matrix_type_{TYPE}_TS_{TEST_SIZE}_RS_{RANDOM_STATE}.txt"), 'w') as f:
    f.write("Confusion Matrix:\n")
    f.write("rows: actual, columns: predicted\n")
    f.write("                          Setosa  Versicolor  Virginica\n")
    for i, species in enumerate(iris.target_names):
        f.write(f"{species:12} {cm[i][0]:7} {cm[i][1]:11} {cm[i][2]:10}\n")
    f.write("\nManual precision, recall, F1-score calculation:\n")
    f.write(f"{species}: Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1_score:.4f}")    
    
plt.figure(figsize=(120,80))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.title(f"Decision Tree for Iris Dataset - {TYPE}, Test Size: {TEST_SIZE}, Random State: {RANDOM_STATE}")

plt.savefig(os.path.join("outputs_1", f"decision_tree_type_{TYPE}_TS_{TEST_SIZE}_RS_{RANDOM_STATE}.png"))
plt.show()