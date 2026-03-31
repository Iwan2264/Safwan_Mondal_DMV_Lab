import matplotlib.pyplot as plt

x = [30, 20, 15, 13, 26, 34]
y = ["Python", "Java", "C++", "JavaScript", "C#", "PHP"]
exp = [0.1, 0, 0, 0, 0, 0]

plt.pie(x, labels=y, explode=exp, autopct='%0.1f%%')

plt.title("Static Pie Chart")

plt.show()