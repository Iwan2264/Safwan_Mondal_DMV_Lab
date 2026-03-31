import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 2, 8, 13, 6]

plt.figure(figsize=(8, 5))

colors = ["red", "blue", "green", "orange", "purple"]
plt.scatter(x, y, color=colors)

plt.title("Static Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.grid(True)
plt.show()