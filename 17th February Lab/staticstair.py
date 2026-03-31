import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(8, 5))

plt.step(x, y, marker='o', color='blue', where='post')

plt.title("Static Stair Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()