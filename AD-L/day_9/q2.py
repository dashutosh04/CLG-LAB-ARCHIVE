import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import os

dir = "./q2"
os.makedirs(dir, exist_ok=True)


wine = load_wine()
X = wine.data
y = wine.target

print("Dataset shape:", X.shape)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

explained_variance = pca.explained_variance_ratio_

print("\nExplained variance by each component:")
for i, var in enumerate(explained_variance):
    print(f"PC{i+1}: {var:.4f}")

plt.figure(figsize=(8,5))
plt.plot(range(1, 14), explained_variance, marker='o')
plt.xlabel("Principal Component")
plt.ylabel("Variance Explained")
plt.title("Variance Explained by PCA Components (Wine Dataset)")
plt.savefig(f"{dir}/pca_variance_wine.png")
plt.show()

pca_2 = PCA(n_components=2)
X_2d = pca_2.fit_transform(X_scaled)

plt.figure(figsize=(8,6))
plt.scatter(X_2d[:,0], X_2d[:,1], c=y)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("2D PCA Projection of Wine Dataset")
plt.savefig(f"{dir}/pca_2d_wine.png")
plt.show()

pca_3 = PCA(n_components=3)
X_3d = pca_3.fit_transform(X_scaled)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_3d[:,0], X_3d[:,1], X_3d[:,2], c=y)

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")
ax.set_title("3D PCA Projection of Wine Dataset")
plt.savefig(f"{dir}/pca_3d_wine.png")
plt.show()