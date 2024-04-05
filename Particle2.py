import numpy as np
import math
import matplotlib.pyplot as plt
class Particle2:
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
        self.x_0 = x_zero
        self.y_0 = y_zero
        vert = math.sqrt(vy_zero**2 + vx_zero**2)
        self.v_0 = vert
        kuto = math.atan2(vy_zero, vx_zero)
        kuti = math.degrees(kuto)
        if vy_zero<0:
            kuti =+ 360
        self.theta = kuti
    def range(self, ddt=None): 
        if ddt is not None:
            self.ddt = ddt  
        self.theta = np.deg2rad(self.theta)
        g = 9.8
        x_zero = self.x_0
        xo = self.x_0
        y_zero = self.y_0
        vx_zero = self.v_0 * math.cos(self.theta)
        vy_zero = self.v_0 * math.sin(self.theta)
        num_vrijeme = 0
        while y_zero >= 0:
            vy_zero = vy_zero - g * self.ddt
            y_zero = y_zero + self.ddt * vy_zero
            x_zero = x_zero + vx_zero * self.ddt
        self.ran = abs(x_zero - xo)
    def rang_ana(self):
        g = 9.8
        x_zero = self.x_0
        y_zero = self.y_0
        kat = self.theta
        vx_zero = self.v_0 * math.cos(self.theta)
        vy_zero = self.v_0 * math.sin(self.theta)
        v_zero = self.v_0
        self.ranp = ( v_zero**2 * math.sin(2*kat) ) / g
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

jan = Particle2(0, 0, 10, 60)
jan.rang_ana()
du = 0
vajs = []
razlika = []
while du<0.1:
    du = du + 0.001
    razlika.append(du)
    jan.range(ddt=du)
    kad = (abs(jan.ranp - jan.ran)/jan.ranp) * 100
    vajs.append(kad)
plt.plot(razlika, vajs)
plt.show()



jan.range(ddt=0.001)
print(jan.ran)
