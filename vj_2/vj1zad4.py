def lin_funkcija(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    
    c = y1 - m * x1
    
    return f"y = {m}x + {c}"

x1, y1 = 1, 8
x2, y2 = 3, 4
primjer = lin_funkcija(x1, y1, x2, y2)
print(primjer)
