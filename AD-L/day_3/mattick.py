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
plt.xticks("X-axis")
plt.yticks("Y-axis")
plt.grid(True)
plt.show()
