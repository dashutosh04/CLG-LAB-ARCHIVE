import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import (
    accuracy_score,
    log_loss,
    confusion_matrix,
    classification_report,
)


save_location = "q1/"
os.makedirs(save_location, exist_ok=True)

mnist = fetch_openml("mnist_784", version=1, as_frame=False, data_home="./data")

X = mnist.data
y = mnist.target.astype(int)

X = X / 255.0

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

svm = SGDClassifier(loss="log_loss", max_iter=1, warm_start=True)

epochs = 10
train_acc = []
val_acc = []
train_loss = []
val_loss = []

classes = np.unique(y_train)

for epoch in range(epochs):
    svm.partial_fit(X_train, y_train, classes=classes)

    y_train_pred = svm.predict(X_train)
    y_val_pred = svm.predict(X_val)

    train_acc.append(accuracy_score(y_train, y_train_pred))
    val_acc.append(accuracy_score(y_val, y_val_pred))

    train_proba = svm.predict_proba(X_train)
    val_proba = svm.predict_proba(X_val)

    train_loss.append(log_loss(y_train, train_proba, labels=range(10)))
    val_loss.append(log_loss(y_val, val_proba, labels=range(10)))

    print(
        f"Epoch {epoch+1}/{epochs} - Train Acc: {train_acc[-1]:.4f}, Val Acc: {val_acc[-1]:.4f}, Train Loss: {train_loss[-1]:.4f}, Val Loss: {val_loss[-1]:.4f}"
    )
    with open(f"{save_location}training_log.txt", "a") as f:
        f.write(
            f"Epoch {epoch+1}/{epochs} - Train Acc: {train_acc[-1]:.4f}, Val Acc: {val_acc[-1]:.4f}, Train Loss: {train_loss[-1]:.4f}, Val Loss: {val_loss[-1]:.4f}\n"
        )

y_test_pred = svm.predict(X_test)

print("\nFinal Test Accuracy:", accuracy_score(y_test, y_test_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_test_pred))
print("\nClassification Report:\n", classification_report(y_test, y_test_pred))


with open(f"{save_location}final_results.txt", "w") as f:
    f.write(f"Final Test Accuracy: {accuracy_score(y_test, y_test_pred):.4f}\n")
    f.write("\nConfusion Matrix:\n")
    f.write(str(confusion_matrix(y_test, y_test_pred)))
    f.write("\n\nClassification Report:\n")
    f.write(classification_report(y_test, y_test_pred))

plt.figure()
plt.plot(range(1, epoch + 2), train_acc, label="Train Accuracy")
plt.plot(range(1, epoch + 2), val_acc, label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("SGD Classifier Accuracy")
plt.legend()
plt.savefig(f"{save_location}accuracy_plot.png")


plt.figure()
plt.plot(range(1, epoch + 2), train_loss, label="Train Loss")
plt.plot(range(1, epoch + 2), val_loss, label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Log Loss")
plt.title("SGD Classifier Log Loss")
plt.legend()
plt.savefig(f"{save_location}loss_plot.png")
