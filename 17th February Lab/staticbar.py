from matplotlib import pyplot as plt

# Static Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 55, 20]

plt.figure(figsize=(6, 5))
plt.bar(categories, values, color='skyblue')

plt.title("Static Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid(axis='y')

plt.show()