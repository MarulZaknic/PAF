import numpy as np
import math
def arithm(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    larithm = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    n = 0
    d = 0
    l = 0
    z = 0
    o = 0
    
    for el in larithm:
        n += 1
        d += el
    g = d/n
    print(g)
def deviacija(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    larithm = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    ko = 0
    k = 0
    d = 0
    n = 0
    o = 0
    l = 0

    for el in larithm:
        n += 1
        d += el
    g = d/n
    for eli in larithm:
        l += 1
        k = (abs(eli - g))**2
        o += k
    ju = l - 1
    e = (o/(l))**(1/2)
    print(e)
arithm(2,10,200,3,4,6,7,3,44,8)
deviacija(2,10,200,3,4,6,7,3,44,8)





