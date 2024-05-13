import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

class planet():
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

    def move(self, lista_tijela):
        G = 6.674 * 10**(-11)
        dt = 10
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

class universe:
    def __init__(self):
        self.lista_tijela = []

    def dodavac_objekata(self, ime, x_p, y_p, z_p, vx_p, vy_p, vz_p, mas):

        ime = planet(x_p, y_p, z_p, vx_p, vy_p, vz_p, mas)
        self.lista_tijela.append(ime)

    def eulerova_simulacija(self):

        def tick():
            for el in self.lista_tijela:
                el.move(self.lista_tijela)
            ax.set_xlim([-30, 30])
            ax.set_ylim([-30, 30])
            ax.set_zlim([-30, 30])
            ax.clear()
            for el in self.lista_tijela:
                ax.scatter(el.vec_r[0], el.vec_r[1], el.vec_r[2], s=el.m)
        ani = FuncAnimation(fig, tick, frames=range(1800), interval=16)
        plt.show()



        
        
# frame delay = 16.67
# frame number = 1800
        

        
uni1 = universe()
uni1.dodavac_objekata("mate", 0, 0, 0, 0, 0, 0, 10)
uni1.dodavac_objekata("šime", 8, 19, 27, 5, 9, 0, 8)
uni1.eulerova_simulacija()

