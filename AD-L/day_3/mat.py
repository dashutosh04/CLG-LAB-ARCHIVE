import matplotlib.pyplot as plt
import numpy as np

plt.plot(
    [1, 2, 3, 4, 5],
    [1, 4, 9, 50, 2],
    marker="o",
    linestyle="--",
    color="r",
    linewidth=2,
)
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
