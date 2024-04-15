import calculus2 as cal
import matplotlib.pylab as plt
import numpy as np
ana_sin = "np.cos(x)"
x1_test = 3
x2_test = 7
analitiÄŤki_rezultat = np.cos(x1_test) - np.cos(x2_test)
rez_num = []
rez_ana = []
stepometar = np.linspace(0, 1000, 10)
for ki in stepometar:
    cal.integral_trap(ana_sin, x1_test, x2_test, ki)
    rez_num.append(rezultat)
smooth_operator = np.arange(0, 1000, 1)
for lo in smooth_operator:
    rez_ana.append(analitiÄŤki_rezultat)
plt.plot(smooth_operator, rez_ana)
plt.scatter(stepometar, rez_num)
plt.show()