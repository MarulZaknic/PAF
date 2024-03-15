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

jed_gibanje(10,20)
