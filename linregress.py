import numpy as np
import matplotlib.pyplot as plt
import math
M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])
D = []
G = []
E = []
for i in range(0,6):
    o = M[i] * phi[i]
    D.append(o)
    u = (phi[i])**2
    al = (M[i])**2
    E.append(al)
    G.append(u)
def prosjek(kad):
    zhar = 0
    for el in kad:
        zhar = zhar + el
    b = len(kad)
    c = zhar / b
    return c
jiu = prosjek(G)
huz = prosjek(D)
a = huz/jiu
plt.scatter(phi,M, label="data")
plt.xlabel("phi vrijednosti")
plt.ylabel("M vrijednosti")
plt.plot(phi, a*phi, label="fit")
plt.show()
rok = prosjek(E)
sigma = np.sqrt((1/6)*((rok/jiu)-a**2))
print("Modul torzije iznosi {} +/- {}".format(a, sigma))












