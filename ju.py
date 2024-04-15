import calculus2 as cal
donja_medja, _ = cal.integral_prav("x**2 + 3*x", 0, 20, 100)
_, gornja_medja = cal.integral_prav("x**2 + 3*x", 0, 20, 100)
print(donja_medja)
print(gornja_medja)