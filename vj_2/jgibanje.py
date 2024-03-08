import matplotlib.pyplot as plt
import numpy as np

def jed_gibanje(masa, sila):
    delta_t = 0.1
    poc_koordinate = 0
    akc = sila / masa
    t_vrijednosti = np.arange(0, 10, 0.1)
    v_vrijednosti = t_vrijednosti * akc   # početna brzina je 0
    p_vrijednosti = ((t_vrijednosti**2) * akc) / 2  # početna brzina i akceleracija su 0
    a_vrijednosti = t_vrijednosti * 0 + akc

    plt.figure(figsize=(8, 4))
    plt.plot(t_vrijednosti, v_vrijednosti, label='brzina')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('brzina (m/s)')
    plt.title('v/t graf')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.plot(t_vrijednosti, p_vrijednosti, label='Položaj')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('položaj (m)')
    plt.title('p/t graf')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.plot(t_vrijednosti, a_vrijednosti, label='Akceleracija')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('akceleracija (m/s^2)')
    plt.title('a/t graf')
    plt.legend()
    plt.grid(True)
    plt.show()

jed_gibanje(10, 50)  






 

