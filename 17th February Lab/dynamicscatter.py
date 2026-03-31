import matplotlib.pyplot as plt
import numpy as np

x = np.array(list(map(float, input("Enter the values for X axis: ").split())))
y = np.array(list(map(float, input("Enter the values for Y axis: ").split())))

plt.figure(figsize=(8, 5))

plt.scatter(x, y, color="blue")

plt.title("Dynamic Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.grid(True)
plt.show()