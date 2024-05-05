import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

class točkasta_masa:
    def __init__(self, x_0, y_0, z_0, vx_0, vy_0, vz_0, m):

        self.x_0 = x_0
        self.y_0 = y_0
        self.z_0 = z_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.vz_0 = vz_0
        self.m = m
        self.vec_r = np.array([x_0, y_0, z_0])
        self.vec_v = np.array([vx_0, vy_0, vz_0])
        lista_tijela.append(self)

    def move(self, lista_tijela):
        G = 9.8
        dt = 0.01
        vec_rr_cm = 0
        uk_m = 0
        for el in lista_tijela:
            if el != self:
                uk_m += el.m
                eli = el.m * el.vec_r
                vec_rr_cm += eli
        vec_r_cm = vec_rr_cm / uk_m
        a_num = (- G * uk_m) / (np.linalg.norm(vec_r_cm - self.vec_r))**3 * (self.vec_r - vec_r_cm)
        self.vec_v = self.vec_v + a_num * dt
        self.vec_r = self.vec_r + self.vec_v * dt


lista_tijela = []
zemlja = točkasta_masa(8, 40, 8, 0, 0, 0, 100)
jupiter = točkasta_masa(-40, -20, 28, 0, 0, 0, 100)
sunce = točkasta_masa(0, 0, 0, 0, 0, 0, 100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    for el in lista_tijela:
        el.move(lista_tijela)
    ax.clear()
    ax.set_xlim([-30, 30])
    ax.set_ylim([-30, 30])
    ax.set_zlim([-30, 30])
    for el in lista_tijela:
        ax.scatter(el.vec_r[0], el.vec_r[1], el.vec_r[2], s=el.m)

ani = FuncAnimation(fig, update, frames=range(100), interval=1)
plt.show()
