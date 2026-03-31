import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter X{i+1}: ")))
    y.append(float(input(f"Enter Y{i+1}: ")))

plt.figure(figsize=(8,5))
plt.plot(x, y, marker='*', linestyle='-', linewidth=2)
plt.xlabel("X Data")
plt.ylabel("Y Data")
plt.title("User Defined Line Graph")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
