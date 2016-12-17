# coding=utf-8
import numpy as np
from time import time

verbose = 2
N = 10

solucion = np.zeros((1, N + 1))


# 0 Sólo errores graves de funcionamiento
# 1 Errores y mensajes resumidos detalle medio
# 2 Detalle máximo
def mensaje(cadena, nivel):
    global verbose
    if nivel <= verbose:
        print(cadena)

def set(posicion, valor):
    global solucion
    solucion[0][posicion] = valor
    mensaje("S%d:%f" % (posicion, valor),2)

def read(posicion):
    global solucion
    mensaje("R%d:%f" % (posicion, solucion[0][posicion]),2)
    return(solucion[0][posicion])

def suma_naturales_original(N):
    global solucion

    for i in range(1, N + 2):
        solucion[0][i - 1] = 0
        for j in range(0, i):
            solucion[0][i - 1] += j

def suma_naturales_profile(N):
    global solucion

    for i in range(1, N + 2):
        set(i - 1, 0)
        for j in range(0, i):
            set(i-1,read(i-1) + j)

def suma_naturales_check(N):
    global solucion

    if solucion[0][1] <> 1.0:
        mensaje("Error verificando 1", 0)
        return (False)
    if solucion[0][2] <> 3.0:
        mensaje("Error verificando 1", 0)
        return (False)
    if solucion[0][3] <> 6.0:
        mensaje("Error verificando 1", 0)
        return (False)
    if solucion[0][4] <> 10.0:
        mensaje("Error verificando 1", 0)
        return (False)
    return (True)

#suma_naturales_original(N)
suma_naturales_profile(N)
if suma_naturales_check(N):
    print(solucion)
