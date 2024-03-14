import matplotlib.pyplot as plt
import numpy as np

def kosi_hitac(v_og, kut):
    theta = np.deg2rad(kut)
    g = 9.8
    x = 0
    y = 0
    vx = v_og * np.cos(theta)
    vy = v_og * np.sin(theta)
    brzina_y = []
    brzina_x = []
    pozicija_x = []
    pozicija_y = []
    
    t_max = 2 * v_og * np.sin(theta) / g
    dt = 0.1
    vrijeme = np.arange(0, t_max, dt)
    
    for t in vrijeme:
        x = x + vx * dt
        pozicija_x.append(x)
        vy = vy - g*dt
        y = y + vy*dt
        pozicija_y.append(y)
    
    plt.subplot(3, 1, 1)
    plt.xlabel("pozicija_x")
    plt.ylabel("pozicija_y")
    plt.plot(pozicija_x, pozicija_y)

    plt.subplot(3, 1, 2)
    plt.xlabel("vrijeme")
    plt.ylabel("pozicija_y")
    plt.plot(vrijeme, pozicija_y)

    plt.subplot(3, 1, 3)
    plt.xlabel("vrijeme")
    plt.ylabel("pozicija_x")
    plt.plot(vrijeme, pozicija_x)
    
    plt.tight_layout()
    plt.show()

kosi_hitac(10, 45)  



