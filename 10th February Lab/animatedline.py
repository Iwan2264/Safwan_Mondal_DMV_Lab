import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o')

ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

def update(frame):
    x_data.append(frame)
    y_data.append(frame * frame)
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=10, interval=300)
plt.show()