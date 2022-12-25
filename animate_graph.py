import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

def animate(num, data, line):
   colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2',   '#7f7f7f', '#bcbd22', '#17becf']
   line.set_color(colors[num % len(colors)])
   line.set_alpha(0.7)
   line.set_data(data[0:2, :num])
   line.set_3d_properties(data[2, :num])
   return line

t = np.arange(0, 20, 0.2)
x = np.cos(t) - 1
y = 1 / 2 * (np.cos(2 * t) - 1)
data = np.array([x, y, t])
N = len(t)
fig = plt.figure()
ax = Axes3D(fig)
ax.axis('off')

line, = plt.plot(data[0], data[1], data[2], lw=7, c='red')
line_ani = animation.FuncAnimation(fig, animate, frames=N, fargs=(data, line), interval=50, blit=False)

plt.show()
