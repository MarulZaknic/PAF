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

    plt.plot(t_vrijednosti, v_vrijednosti, label='Continuous Line')
    plt.xlabel('v_vrijednosti')
    plt.ylabel('t_vrijednosti')
    plt.title('v/t_graf')
    plt.legend()
    plt.grid(True)

    plt.plot(t_vrijednosti, p_vrijednosti, label='Continuous Line')
    plt.xlabel('p_vrijednosti')
    plt.ylabel('t_vrijednosti')
    plt.title('p/t_graf')
    plt.legend()
    plt.grid(True)

    plt.plot(t_vrijednosti, a_vrijednosti, label='Continuous Line')
    plt.xlabel('a_vrijednosti')
    plt.ylabel('t_vrijednosti')
    plt.title('a/t_graf')
    plt.legend()
    plt.grid(True)
    plt.show()

jed_gibanje(20,5)



 

