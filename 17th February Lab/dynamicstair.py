import matplotlib.pyplot as plt
import numpy as np

x = np.array(list(map(int, input("Enter the value of X axis: ").split())))
y = np.array(list(map(int, input("Enter the values of Y axis: ").split())))

plt.figure(figsize=(8, 9))

plt.step(x, y, marker='o', color='blue', where='post')

plt.title("Dynamic Stair Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.grid(True)
plt.show()