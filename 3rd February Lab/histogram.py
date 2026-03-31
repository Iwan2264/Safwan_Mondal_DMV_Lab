import matplotlib.pyplot as plt
import numpy as np

data = np.random.uniform(0, 50, 200)

plt.hist(data, bins=15, color='cyan', edgecolor='red')
plt.xlabel("Range")
plt.ylabel("Count")
plt.title("Histogram - Uniform Data")
plt.show()
