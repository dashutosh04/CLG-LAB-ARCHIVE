import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import (
    accuracy_score,
    log_loss,
    confusion_matrix,
    classification_report,
)
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
from skimage.io import imread
from skimage.transform import resize


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
save_location = os.path.join(SCRIPT_DIR, "q4")
os.makedirs(save_location, exist_ok=True)


print("Loading MNIST...")
mnist = fetch_openml("mnist_784", version=1, as_frame=False)

X = mnist.data / 255.0
y = mnist.target.astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

svm = SGDClassifier(loss="log_loss", max_iter=1, warm_start=True, random_state=42)

epochs = 10
train_acc, val_acc = [], []
train_loss, val_loss = [], []

classes = np.unique(y_train)

for epoch in range(epochs):

    X_train, y_train = shuffle(X_train, y_train, random_state=epoch)

    svm.partial_fit(X_train, y_train, classes=classes)

    y_train_pred = svm.predict(X_train)
    y_val_pred = svm.predict(X_val)

    train_acc.append(accuracy_score(y_train, y_train_pred))
    val_acc.append(accuracy_score(y_val, y_val_pred))

    train_proba = svm.predict_proba(X_train)
    val_proba = svm.predict_proba(X_val)

    train_loss.append(log_loss(y_train, train_proba))
    val_loss.append(log_loss(y_val, val_proba))

    print(
        f"Epoch {epoch+1}/{epochs} - "
        f"Train Acc: {train_acc[-1]:.4f}, Val Acc: {val_acc[-1]:.4f}, "
        f"Train Loss: {train_loss[-1]:.4f}, Val Loss: {val_loss[-1]:.4f}"
    )

y_test_pred = svm.predict(X_test)

print("\nFinal Test Accuracy:", accuracy_score(y_test, y_test_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_test_pred))
print("\nClassification Report:\n", classification_report(y_test, y_test_pred))

plt.figure()
plt.plot(range(1, epochs + 1), train_acc, label="Train Accuracy")
plt.plot(range(1, epochs + 1), val_acc, label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("SGD Classifier Accuracy (MNIST)")
plt.legend()
plt.grid()
plt.savefig(os.path.join(save_location, "accuracy_plot.png"))
plt.show()

plt.figure()
plt.plot(range(1, epochs + 1), train_loss, label="Train Loss")
plt.plot(range(1, epochs + 1), val_loss, label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Log Loss")
plt.title("SGD Classifier Log Loss (MNIST)")
plt.legend()
plt.grid()
plt.savefig(os.path.join(save_location, "loss_plot.png"))
plt.show()


DATASET_PATH = os.path.join(SCRIPT_DIR, "melanoma_cancer_dataset")
IMG_SIZE = 32


def load_skin_dataset(path):
    X, y = [], []
    classes = {"benign": 0, "malignant": 1}

    split_dirs = [d for d in ["train", "test"] if os.path.isdir(os.path.join(path, d))]
    if split_dirs:
        base_dirs = [os.path.join(path, d) for d in split_dirs]
    else:
        base_dirs = [path]

    for base in base_dirs:
        for label in classes:
            folder = os.path.join(base, label)
            if not os.path.isdir(folder):
                continue

            for file in os.listdir(folder):
                img_path = os.path.join(folder, file)
                try:
                    img = imread(img_path)

                    if img.ndim == 3:
                        img = img.mean(axis=2)

                    img = resize(img, (IMG_SIZE, IMG_SIZE))
                    X.append(img.flatten())
                    y.append(classes[label])
                except:
                    pass

    return np.array(X), np.array(y)


print("\nLoading Skin Cancer Dataset...")
X_skin, y_skin = load_skin_dataset(DATASET_PATH)

print("Samples:", X_skin.shape)

if X_skin.shape[0] == 0:
    raise FileNotFoundError(
        "No skin cancer images found. "
        f"Expected benign/malignant under {DATASET_PATH}"
    )


X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_skin, y_skin, test_size=0.2, random_state=42, stratify=y_skin
)


pipeline = Pipeline([("scaler", StandardScaler()), ("svm", LinearSVC())])

param_grid = {"svm__C": [0.1, 1, 10]}

grid = GridSearchCV(
    pipeline, param_grid, cv=2, scoring="accuracy", n_jobs=-1, verbose=1
)

print("\nRunning Fast GridSearchCV for Skin Cancer SVM...")
grid.fit(X_train_s, y_train_s)

print("\nBest Parameters:", grid.best_params_)

best_model = grid.best_estimator_

y_pred_skin = best_model.predict(X_test_s)

print("\nSkin Cancer SVM Accuracy:", accuracy_score(y_test_s, y_pred_skin))
print("\nConfusion Matrix:\n", confusion_matrix(y_test_s, y_pred_skin))
print("\nClassification Report:\n", classification_report(y_test_s, y_pred_skin))

with open(os.path.join(save_location, "skin_cancer_results.txt"), "w") as f:
    f.write(f"Best Parameters: {grid.best_params_}\n")
    f.write(f"Test Accuracy: {accuracy_score(y_test_s, y_pred_skin):.4f}\n")
    f.write("\nConfusion Matrix:\n")
    f.write(str(confusion_matrix(y_test_s, y_pred_skin)))
    f.write("\n\nClassification Report:\n")
    f.write(classification_report(y_test_s, y_pred_skin))
    
