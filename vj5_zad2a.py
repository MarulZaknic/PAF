import calculus2 as cal
import matplotlib.pyplot as plt
import numpy as np

ana_kvadrat = "x**2"
x1_test = 3
x2_test = 7
analiticki_rezultat = ((x2_test**3)/3) - ((x1_test**3)/3)
rez_num = []
rez_ana = []
rez_num_g = []
rez_num_d = []

stepometar = np.linspace(0, 1000, 20, dtype=int)

for ki in stepometar:
    rezultat, _ = cal.integral_trap(ana_kvadrat, x1_test, x2_test, ki)
    rez_num.append(rezultat)
    donja_medja, _ = cal.integral_prav(ana_kvadrat, x1_test, x2_test, ki)
    rez_num_d.append(donja_medja)
    _, gornja_medja = cal.integral_prav(ana_kvadrat, x1_test, x2_test, ki)
    rez_num_g.append(gornja_medja)
rez_ana = [analiticki_rezultat] * len(stepometar)   #baza nacin za funkcije koje ne mjenjaju vrijednosti
#print("This",analiticki_rezultat)
#print(rez_num_g)

plt.plot(stepometar, rez_ana, label='analiticko')
plt.scatter(stepometar, rez_num, label='numericko')
plt.scatter(stepometar, rez_num_d, label ="donja medja")
plt.scatter(stepometar, rez_num_g, label ="gornja medja")
plt.xlabel('Broj koraka')
plt.ylabel('vrijednost integrala')
plt.legend()
plt.title('Usporedba rjesenja')
plt.show()
