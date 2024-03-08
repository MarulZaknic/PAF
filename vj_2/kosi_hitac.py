import numpy as np
import matplotlib.pyplot as plt

def kosi_hitac(v0, theta, g=9.81, delta_t=0.01):
    theta_rad = np.radians(theta)
    t_flight = 2 * v0 * np.sin(theta_rad) / g
    t_max = min(t_flight, 10)
    t = np.arange(0, t_max, delta_t)
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    return x, y, t

v0 = 20  
theta = 45  

x, y, t = kosi_hitac(v0, theta)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x/y graf')
plt.grid(True)
plt.show()

plt.plot(t, x)
plt.xlabel('t')
plt.ylabel('x')
plt.title('x/t graf')
plt.grid(True)
plt.show()

plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('y/t graf')
plt.grid(True)
plt.show()

kosi_hitac(20, 10)