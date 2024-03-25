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
        delta_t = 7
        self.theta = np.deg2rad(self.theta)
        g = 9.8
        dt = 0.01
        x_zero = self.x_0
        y_zero = self.y_0
        vx_zero = self.v_0 * math.cos(self.theta)
        vy_zero = self.v_0 * math.sin(self.theta)
        mover = np.arange(0, delta_t, dt)
        for e in mover:
            if y_zero>0:
                  x_zero = x_zero + dt * vx_zero
                  vy_zero = vy_zero - g*dt
                  y_zero = y_zero + dt * vy_zero
    def range(self):
        self.theta = np.deg2rad(self.theta)
        g = 9.8
        dt = 0.01
        x_zero = self.x_0
        xo = self.x_0
        y_zero = self.y_0
        vx_zero = self.v_0 * math.cos(self.theta)
        vy_zero = self.v_0 * math.sin(self.theta)
        v_tru = self.v_0
        num_vrijeme = 0
        while y>0:
            vy_zero = vy_zero - g*dt
            y_zero = y_zero + dt * vy_zero
            num_vrijeme = num_vrijeme + dt
        for i in range(0, num_vrijeme, dt):
            xo = xo + dt * vx_zero
        Ran = abs(xo - x_zero)
        print(Ran)
    def plot_trajectory(self):
        self.theta = np.deg2rad(self.theta)
        g = 9.8
        dt = 0.01
        x_zero = self.x_0
        y_zero = self.y_0
        vx_zero = self.v_0 * math.cos(self.theta)
        vy_zero = self.v_0 * math.sin(self.theta)
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