import matplotlib.pyplot as plt
import numpy as np

x = []
for i in range(1, 50):
    x.append(i)
y = [value * 3 for value in x]
print("values of x:")
print(x)
print("values of y thrice of x:")
print(y)

plt.plot(x, y, marker="x", color="r", linewidth=2)
plt.title("Line Graph of y=3x")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
