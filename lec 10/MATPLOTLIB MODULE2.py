import matplotlid.pyplot as plt
import numpy as np
import matplotlid.animation as animation

fig, ax = plt.subplots()

x = np.linespace(0, 2 *np.pi, 100)
y = np.sin(x)


line, = ax.plote(x,y)

def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,
ani = animation.Funcanimation(fig, update, frames=100, intrval=50, blit=True)
plt.show()