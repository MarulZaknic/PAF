import numpy as np
def jed_trecina(N):
    a = 0
    b = 5
    i = 0
    h = 0
    while i<N:
        a = a + (1/3)
        i += 1
    while h<N:
        b = b - (1/3)
        h += 1
    print(a)
    print(b)
jed_trecina(200)

