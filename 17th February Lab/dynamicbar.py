from matplotlib import pyplot as plt
import numpy as np

n = int(input("Enter number of categories: "))

categories = np.array(list(map(str, input("Enter the categories: ").split())))
values = np.array(list(map(int, input("Enter the values for each category: ").split())))

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='red')

plt.title("Dynamic Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid(axis='y')

plt.show()