import json
import matplotlib.pyplot as plt 
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("spambase.csv")
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values


os.makedirs("outputs_2", exist_ok=True)

config_file = "config.json"

with open(config_file, 'r') as f:
    config = json.load(f)
    
TEST_SIZE = config.get("test_size")
TYPE = config.get("type")
RANDOM_STATE = config.get("random_state", 42)
MAX_DEPTH = config.get("max_depth", 4)

new_df = df.dropna()

s = (new_df.dtypes == 'object')
object_cols = list(s[s].index)
print("categorical variables:")
print(object_cols)
print("No. of categorical variables:",len(object_cols) )
OH_encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
OH_cols = pd.DataFrame(OH_encoder.fit_transform(new_df[object_cols]))
OH_cols.index = new_df.index
OH_cols.columns = OH_encoder.get_feature_names_out()
df_final = new_df.drop(object_cols, axis=1)
df_final = pd.concat([df_final, OH_cols], axis=1)

df = df_final

if TYPE == 1:
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE, random_state=RANDOM_STATE,stratify=y)
    clf = DecisionTreeClassifier(random_state=RANDOM_STATE,max_depth=MAX_DEPTH)
elif TYPE == 2:
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)
    clf = DecisionTreeClassifier(random_state=RANDOM_STATE,max_depth=MAX_DEPTH)
else:
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE)
    clf = DecisionTreeClassifier(max_depth=MAX_DEPTH)


clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}%")

print("Classification Report:")
print(classification_report(y_test, y_pred,target_names=["Not Spam", "Spam"]))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print("rows: actual, columns: predicted")
print("                          Not Spam  Spam")
for i, species in enumerate(["Not Spam", "Spam"]):
    print(f"{species:12} {cm[i][0]:7} {cm[i][1]:11}")
    
    
print("Manual precision, recall, F1-score calculation:")

precision = recall = f1_score = 0

for i, species in enumerate(["Not Spam", "Spam"]):
    TP = cm[i][i]
    FP = sum(cm[:,i]) - TP
    FN = sum(cm[i,:]) - TP
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    print(f"{species}: Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1_score:.4f}")    

with open(os.path.join("outputs_2", f"confusion_matrix_type_{TYPE}_TS_{TEST_SIZE}_RS_{RANDOM_STATE}_MD_{MAX_DEPTH}.txt"), 'w') as f:
    f.write("Confusion Matrix:\n")
    f.write("rows: actual, columns: predicted\n")
    f.write("                          Not Spam  Spam\n")
    for i, species in enumerate(["Not Spam", "Spam"]):
        f.write(f"{species:12} {cm[i][0]:7} {cm[i][1]:11}\n")
    f.write("\nManual precision, recall, F1-score calculation:\n")
    f.write(f"{species}: Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1_score:.4f}")    
    
plt.figure(figsize=(12,8))
plot_tree(clf, filled=True, feature_names=df.columns[:-1], class_names=["Not Spam", "Spam"])
plt.title(f"Decision Tree for SpamBase Dataset - {TYPE}, Test Size: {TEST_SIZE}, Random State: {RANDOM_STATE}, Max Depth: {MAX_DEPTH}")

plt.savefig(os.path.join("outputs_2", f"decision_tree_type_{TYPE}_TS_{TEST_SIZE}_RS_{RANDOM_STATE}_MD_{MAX_DEPTH}.png"))
plt.show()