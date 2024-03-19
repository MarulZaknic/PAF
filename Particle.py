import numpy as np
import math
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,x_0, y_0, v_0, theta):
        self.x_0 = x_0
        self.y_0 = y_0
        self.v_0 = v_0
        self.theta = theta
    def reset(self):
        self.x_0 = 0
        self.y_0 = 0
        self.v_0 = 0
        self.theta = 0
    def __move(self):
        delta_x = 7
        self.x_0 = self.x_0 + delta_x
    def range(self):
        self.theta = np.deg2rad(self.theta)
        g = 9.8
        D = (self.v_0**2 * math.sin(2 * self.theta) / g) + (self.x_0 * math.sin(self.theta) * math.cos(self.theta) / g)
    def putanja(self):
        self.theta = np.deg2rad(self.theta)
        g = 9.8
        dt = 0.01
        x_zero = self.x_0
        y_zero = self.y_0
        vx_zero = self.v_0 * math.cos(theta)
        vy_zero = self.v_0 * math.sin(theta)
        v_tru = self.v_0
        pozicija_x = []
        pozicija_y = []
        while y_zero>0:
            x_zero = x_zero + dt * vx_zero
            pozicija_x.append(x_zero)
            vy_zero = vy_zero - g*dt
            y_zero = y_zero + dt * vy_zero
            pozicija_y.append(y_zero)
        plt.plot(pozicija_x, pozicija_y)
        plt.xlabel("pozicija x")
        plt.ylabel("pozicija y")
        plt.show()




            




        






        


