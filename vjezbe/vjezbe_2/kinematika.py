import matplotlib.pyplot as plt
import numpy as np

def jed_gibanje(N,m):
    a = N/m
    vrijeme = np.arange(0,10,0.1)
    polozaj = []
    brzina = []
    akceleracija = []

    dt = 0.1
    x = 0     #poč uvjet položaja je 0
    v = 0     #poč. uvjet brzine je 0
    for i in vrijeme:
        v = v + a*dt
        brzina.append(v)
        x = x + v*dt
        polozaj.append(x)
        akceleracija.append(a)
    plt.subplot(3,1,1)
    plt.xlabel("vrijeme")
    plt.ylabel("položaj")
    plt.plot(vrijeme, polozaj)

    plt.subplot(3,1,2)
    plt.xlabel("vrijeme")
    plt.ylabel("brzina")
    plt.plot(vrijeme, brzina)

    plt.subplot(3,1,3)
    plt.xlabel("vrijeme")
    plt.ylabel("akceleracija")
    plt.plot(vrijeme, akceleracija)
    plt.show()

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
