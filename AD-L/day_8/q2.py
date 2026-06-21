import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, hinge_loss

save_location = "q2/"
os.makedirs(save_location, exist_ok=True)

mnist = fetch_openml("mnist_784", version=1, as_frame=False, data_home="./dataq2")
X = mnist.data / 255.0
y = mnist.target.astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

svm = SGDClassifier(loss="hinge", max_iter=1, warm_start=True)

epochs = 10
train_acc, val_acc = [], []
train_loss, val_loss = [], []

classes = np.unique(y_train)

for epoch in range(epochs):
    svm.partial_fit(X_train, y_train, classes=classes)

    y_train_pred = svm.predict(X_train)
    y_val_pred = svm.predict(X_val)

    train_acc.append(accuracy_score(y_train, y_train_pred))
    val_acc.append(accuracy_score(y_val, y_val_pred))

    train_decision = svm.decision_function(X_train)
    val_decision = svm.decision_function(X_val)

    train_loss.append(hinge_loss(y_train, train_decision))
    val_loss.append(hinge_loss(y_val, val_decision))

    print(
        f"Epoch {epoch+1}/10 - Train Acc: {train_acc[-1]:.4f}, Val Acc: {val_acc[-1]:.4f}"
    )

y_test_pred = svm.predict(X_test)
print("Final Test Accuracy:", accuracy_score(y_test, y_test_pred))

plt.figure()
plt.plot(range(1, epochs + 1), train_acc, label="Train Accuracy")
plt.plot(range(1, epochs + 1), val_acc, label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Linear SVM Accuracy")
plt.legend()
plt.savefig(f"{save_location}accuracy.png")

plt.figure()
plt.plot(range(1, epochs + 1), train_loss, label="Train Loss")
plt.plot(range(1, epochs + 1), val_loss, label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Hinge Loss")
plt.title("Linear SVM Loss")
plt.legend()
plt.savefig(f"{save_location}loss.png")

with open(f"{save_location}final_results.txt", "w") as f:
    f.write(f"Final Test Accuracy: {accuracy_score(y_test, y_test_pred):.4f}\n")
    f.write("\nClassification Report:\n")
    f.write(classification_report(y_test, y_test_pred))
    
