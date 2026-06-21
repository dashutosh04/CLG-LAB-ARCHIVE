import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

df = pd.read_csv("Mall_Customers.csv")

print("First 5 rows of dataset:")
print(df.head())


X = df[["Annual Income (k$)", "Spending Score (1-100)"]]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

df["Cluster"] = clusters


centroids = kmeans.cluster_centers_


plt.figure(figsize=(8, 6))

plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap="viridis", s=50)
plt.scatter(centroids[:, 0], centroids[:, 1], c="red", s=200, marker="X")

plt.xlabel("Scaled Annual Income")
plt.ylabel("Scaled Spending Score")
plt.title("K-Means Clustering of Customers")
plt.savefig("./q1/customer_clusters.png")
plt.show()


print("\nCluster-wise Mean Values:")
cluster_analysis = df.groupby("Cluster")[
    ["Annual Income (k$)", "Spending Score (1-100)"]
].mean()
print(cluster_analysis)


print("\nNumber of customers in each cluster:")
print(df["Cluster"].value_counts())

save_path = "./q1"
os.makedirs(save_path, exist_ok=True)
cluster_analysis.to_csv(f"{save_path}/cluster_analysis.csv")

for i in range(5):
    file = open(f"{save_path}/cluster_{i}_analysis.txt", "w")

    income = cluster_analysis.iloc[i][0]
    spending = cluster_analysis.iloc[i][1]

    print(f"\nCluster {i} Analysis:")
    file.write(f"Cluster {i} Analysis:\n")
    file.write(f"Average Income: {income}\n")
    file.write(f"Average Spending Score: {spending}\n")

    if income > 60 and spending > 60:
        file.write("-> High Income, High Spending (Premium Customers)\n")
        print("-> High Income, High Spending (Premium Customers)")
    elif income < 40 and spending < 40:
        file.write("-> Low Income, Low Spending (Budget Customers)\n")
        print("-> Low Income, Low Spending (Budget Customers)")
    elif income > 60 and spending < 40:
        file.write("-> High Income, Low Spending (Conservative Customers)\n")
        print("-> High Income, Low Spending (Conservative Customers)")
    elif income < 40 and spending > 60:
        file.write("-> Low Income, High Spending (Impulsive Buyers)\n")
        print("-> Low Income, High Spending (Impulsive Buyers)")
    else:
        file.write("-> Medium Income & Medium Spending (Average Customers)\n")
        print("-> Medium Income & Medium Spending (Average Customers)")

    file.close()


save_path = "./q1"
