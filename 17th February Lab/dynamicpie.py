import matplotlib.pyplot as plt
import numpy as np

x = np.array(list(map(float, input("Enter the values: ").split())))
y = np.array(list(map(str, input("Enter the labels: ").split())))
exp = np.array(list(map(float, input("Enter the explode values: ").split())))

plt.pie(x, labels=y, explode=exp, autopct='%0.1f%%')

plt.title("Dynamic Pie Chart")

plt.show()