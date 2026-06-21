import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, log_loss
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle

save_location = "q3/"
os.makedirs(save_location, exist_ok=True)

mnist = fetch_openml("mnist_784", version=1, as_frame=False, data_home="./dataq3")
X = mnist.data.astype(np.float32) / 255.0
y = mnist.target.astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

epochs = 10
batch_size = 8000
train_acc, val_acc = [], []
train_loss, val_loss = [], []

for epoch in range(1, epochs + 1):
    X_train, y_train = shuffle(X_train, y_train, random_state=epoch)
    X_batch = X_train[:batch_size]
    y_batch = y_train[:batch_size]

    svm = SVC(kernel="rbf", max_iter=2000)
    svm.fit(X_batch, y_batch)

    y_train_pred = svm.predict(X_batch)
    y_val_pred = svm.predict(X_val)

    train_acc.append(accuracy_score(y_batch, y_train_pred))
    val_acc.append(accuracy_score(y_val, y_val_pred))

    train_scores = svm.decision_function(X_batch)
    val_scores = svm.decision_function(X_val)

    train_prob = np.exp(train_scores) / np.sum(np.exp(train_scores), axis=1, keepdims=True)
    val_prob = np.exp(val_scores) / np.sum(np.exp(val_scores), axis=1, keepdims=True)

    train_loss.append(log_loss(y_batch, train_prob))
    val_loss.append(log_loss(y_val, val_prob))

    print(f"Epoch {epoch}/10 - Train Acc: {train_acc[-1]:.4f}, Val Acc: {val_acc[-1]:.4f}")

y_test_pred = svm.predict(X_test)
print("Final Test Accuracy:", accuracy_score(y_test, y_test_pred))

plt.figure()
plt.plot(range(1, epochs + 1), train_acc, label="Train Accuracy")
plt.plot(range(1, epochs + 1), val_acc, label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("RBF SVM Accuracy")
plt.legend()
plt.savefig(f"{save_location}accuracy.png")

plt.figure()
plt.plot(range(1, epochs + 1), train_loss, label="Train Loss")
plt.plot(range(1, epochs + 1), val_loss, label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Log Loss")
plt.title("RBF SVM Loss")
plt.legend()
plt.savefig(f"{save_location}loss.png")

with open(f"{save_location}final_results.txt", "w") as f:
    f.write(f"Final Test Accuracy: {accuracy_score(y_test, y_test_pred):.4f}\n")
    f.write("\nClassification Report:\n")
    f.write(classification_report(y_test, y_test_pred))