
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

