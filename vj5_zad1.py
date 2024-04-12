import calculus as cal
import numpy as np
import matplotlib.pyplot as plt
ana_sinus = np.cos(4)
ana_kub = 3*4**2
h_values = [0.1, 0.01, 0.001]
sin_num_values = []
kub_num_values = []
for h in h_values:
    sin_num = cal.derivacija("np.sin(x)", 4, h, "2step")
    sin_num_values.append(sin_num)
    kub_num = cal.derivacija("x**3", 4, h, "2step")
    kub_num_values.append(kub_num)
plt.figure(figsize=(10, 6))
plt.scatter(h_values, sin_num_values, label='numeričko rješenje (sin(x))')
plt.scatter(h_values, kub_num_values, label='numeričko rješenje (x^3)')
plt.axhline(y=ana_sinus, color='r', linestyle='--', label='analitičko rješenje (cos(4))')
plt.axhline(y=ana_kub, color='g', linestyle='--', label='anlitičko rješenje (4^3)')
plt.xlabel('Step Size (h)')
plt.ylabel('Derivative')
plt.title('Numerical and Analytical Solutions of Derivatives')
plt.legend()
plt.show()


