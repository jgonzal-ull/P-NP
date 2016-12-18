# coding=utf-8
import numpy as np
from time import time

verbose = 2
N = 4
Nnum = 20

solucion = np.zeros((1, N + 1))
numeros = np.zeros((1,Nnum))
indices = np.zeros((1,10))


for i in range(0,Nnum):
    numeros[0][i] = i
# 0 Sólo errores graves de funcionamiento
# 1 Errores y mensajes resumidos detalle medio
# 2 Detalle máximo
def mensaje(cadena, nivel):
    global verbose
    if nivel <= verbose:
        print(cadena)

def set_solucion(posicion, valor):
    global solucion
    solucion[0][posicion] = valor
    mensaje("SS%d:%f" % (posicion, valor),2)
def set_indice(posicion, valor):
    global indices
    indices[0][posicion] = valor
    mensaje("SI%d:%f" % (posicion, valor),2)
def set_numero(posicion, valor):
    global numeros
    numeros[0][posicion] = valor
    mensaje("SN%d:%f" % (posicion, valor),2)

def read_solucion(posicion):
    global solucion
    mensaje("RS%d:%f" % (posicion, solucion[0][posicion]),2)
    return(solucion[0][posicion])
def read_indice(posicion):
    global indices
    mensaje("RI%d:%f" % (posicion, indices[0][posicion]),2)
    return(indices[0][posicion])
def read_numero(posicion):
    global numeros
    mensaje("RN%d:%f" % (posicion, numeros[0][posicion]),2)
    return(numeros[0][posicion])

def suma_naturales_original(N):
    global solucion

    for i in range(1, N + 2):
        solucion[0][i - 1] = 0
        for j in range(0, i):
            solucion[0][i - 1] += j

def suma_naturales_profile(N):
    global solucion

    set_indice(0,1)
    for i in range(1, N + 2):
        read_indice(0)
        set_solucion(i - 1, 0)
        set_indice(1,0)
        for j in range(0, i):
            read_indice(1)
            set_solucion(i-1,read_solucion(i-1) + read_numero(j))
            set_indice(1,read_indice(1)+read_numero(1))
        set_indice(0,read_indice(0)+read_numero(1))

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
