import matplotlib.pyplot as plt
import numpy as np

def derivacija(funk_str, točka, h, metoda):
    funk = eval("lambda x: " + funk_str)
    x_float = float(točka)
    if metoda == "2step":
        derivacija = (funk(x_float + h) - funk(x_float)) / h
    elif metoda == "3step":
        derivacija = (funk(x_float + h) - funk(x_float - h)) / (2 * h)
    return derivacija

def derivacija_adv(funk_str, točka1, točka2, h, metoda):
    funk = eval("lambda x: " + funk_str)
    x1_float = float(točka1)
    x2_float = float(točka2)
    arti = x1_float
    numder_lista = []
    inputi = []
    inputi.append(arti)
    while arti <= x2_float:
        if metoda == "2step":
            derivacija = (funk(arti + h)) - funk(arti) / h
        elif metoda == "3step":
            derivacija = (funk(arti + h) - funk(arti - h)) / (2 * h)
        numder_lista.append(derivacija)
        arti = arti + h
        inputi.append(arti)
    return numder_lista, inputi

def integral_prav(funk_str, točka1, točka2, h):
    funk = eval("lambda x: " + funk_str)
    x1_float = float(točka1)
    x2_float = float(točka2)
    gornja_medja = 0
    donja_medja = 0
    ui = (x2_float - x1_float) / h
    ar_donja = np.linspace(x1_float, x2_float - ui, h)
    ar_gornja = np.linspace(x1_float + ui, x2_float, h)
    for u in ar_donja:
        snip = funk(u)*ui
        donja_medja = donja_medja + snip
    for l in ar_gornja:
        snup = funk(l)*ui
        gornja_medja = gornja_medja + snup
    return donja_medja, gornja_medja
def integral_trap(funk_str, točka1, točka2, h):
    rezultat = 0
    funk = eval("lambda x: " + funk_str)
    x1_float = float(točka1)
    x2_float = float(točka2)
    ar_vrh = np.linspace(x1_float, x2_float, h)
    rez_trap = []
    ui = (x2_float - x1_float) / h
    verdi = x1_float
    for ap in ar_vrh:
        trap = (funk(verdi + ui) + funk(verdi)) / 2 * ui
        rez_trap.append(trap)
        verdi = verdi + ui
        rezultat = rezultat + trap
    return rezultat, rez_trap
