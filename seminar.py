import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

class svemir:
    def __init__(self):
        self.lista_planeta = []

    def dodavac_planeta(self, x, y, z, vx, vy, vz, masa, ime):
        novi_planet = planet(x, y, z, vx, vy, vz, masa, self, ime)
        return novi_planet

    def simulacija(self, steps, interval):
        def provjera_evolucije(r,r_prev, po, n):
            dot_prev = np.dot(r_prev - po,n)
            dot_sad = np.dot(r - po,n)
            if dot_prev * dot_sad < 0:
                return(True)
            else:
                return(False)
                
        xmax = ymax = zmax = 0
        for el in self.lista_planeta:
            if el.vec_r[0] > xmax:
                xmax = el.vec_r[0]
            if el.vec_r[1] > ymax:
                ymax = el.vec_r[1]
            if el.vec_r[2] > zmax:
                zmax = el.vec_r[2]
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        def update(frame):
            for el in self.lista_planeta:
                el.move()
                if provjera_evolucije(el.vec_r,el.vec_rpros, el.vec_rpoc, el.vec_norm) == True:
                    el.evocount += 1
                if el.evocount < 2:
                    el.evosecound += 10000
            ax.clear()
            ax.set_xlim([-2.4 * (10**11), 2.4 * (10**11) ])
            ax.set_ylim([-2.4 * (10**11), 2.4 * (10**11) ])
            ax.set_zlim([-2.4 * (10**11), 2.4 * (10**11) ])
            for el in self.lista_planeta:
                ax.scatter([el.vec_r[0]], [el.vec_r[1]], [el.vec_r[2]])



        ani = FuncAnimation(fig, update, frames=range(steps), interval=interval)
        plt.show()
        for el in self.lista_planeta:
            print("Numerički iznos evolucije je ", el.evosecound)

class planet:
    def __init__(self, x_0, y_0, z_0, vx_0, vy_0, vz_0, m, svemir_instance, ime):
        self.vec_r = np.array([x_0, y_0, z_0])
        self.vec_v = np.array([vx_0, vy_0, vz_0])
        self.svemir_instance = svemir_instance
        self.m = m
        self.svemir_instance.lista_planeta.append(self)
        self.vec_rpoc = np.array([x_0, y_0, z_0])
        self.vec_norm = self.vec_v / np.linalg.norm(self.vec_v)
        self.evocount = 0
        self.evosecound = 0
        self.ime = str(ime)

    def move(self):
        G = 6.674 * (10**(-11))
        dt = 100000
        vec_rr_cm = 0
        uk_m = 0
        for el in self.svemir_instance.lista_planeta:
            if el != self:
                uk_m += el.m
                eli = el.m * el.vec_r
                vec_rr_cm += eli
        vec_r_cm = vec_rr_cm / uk_m
        self.vec_rpros = self.vec_r
        a_num = (- G * uk_m) / (np.linalg.norm(vec_r_cm - self.vec_r))**3 * (self.vec_r - vec_r_cm)
        self.vec_v = self.vec_v + a_num * dt
        self.vec_r = self.vec_r + self.vec_v * dt

uni1 = svemir()
uni1.dodavac_planeta(1.495*(10**11),0,0,0,2.972 * (10**4),0,5.972 * (10**24), "zemlja")             ### zemlja ###(1.495*(10**11),0,0,0,2.972 * (10**4),0,5.972 * (10**24))
uni1.dodavac_planeta(5.6197 * (10**10),0,0,0,4.787 * (10**4),0,3.285*(10**23), "mercury")                                                                   ### merkur ###(5.6197 * (10**10),0,0,0,6.138 * (10**8),0,3.285*(10**23))
uni1.dodavac_planeta(1.082 * (10**11),0,0,0,3.502 * (10**4),0,4.867 * (10**24), "venera")                                                              ### venera ###(1.082 * (10**11),0,0,0,3.502 * (10**4),0,4.867 * (10**24))
uni1.dodavac_planeta(2.0827 * (10**11),0,0,0,2.407 * (10**4),0,6.39 * (10**23), "mars")                                                                   ### mars ###()
uni1.dodavac_planeta(0,0,0,0,0,0,1.989 * (10**30), "sunce")
#uni1.dodavac_planeta(10, 0, 0, 0, 0 ,0 ,1)
#uni1.dodavac_planeta(0, 0, 0, 0, 0, 0, 10 )
#uni1.dodavac_planeta(5,28, 6, 0, 0, 0, 69)                                        ### sunce ### (0,0,0,0,0,0,1.989 * (10**30))
uni1.simulacija(steps=100, interval=10)
