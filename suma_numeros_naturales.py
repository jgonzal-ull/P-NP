# coding=utf-8
import numpy as np
from funciones import *
from time import time

verbose = 0
Nnum = 100

solucion = np.zeros((1, Nnum + 1))
numeros = np.zeros((1,Nnum))
indices = np.zeros((1,Nnum))

secuencia=[]

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
    global solucion, secuencia
    solucion[0][posicion] = valor
    mensaje("SS%d:%f" % (posicion, valor),2)
    secuencia.append("SS%d:%f" % (posicion, valor))
def set_indice(posicion, valor):
    global indices, secuencia
    indices[0][posicion] = valor
    mensaje("SI%d:%f" % (posicion, valor),2)
    secuencia.append("SI%d:%f" % (posicion, valor))
def set_numero(posicion, valor):
    global numeros, secuencia
    numeros[0][posicion] = valor
    mensaje("SN%d:%f" % (posicion, valor),2)
    secuencia.append("SN%d:%f" % (posicion, valor))
def read_solucion(posicion):
    global solucion, secuencia
    mensaje("RS%d:%f" % (posicion, solucion[0][posicion]),2)
    secuencia.append("RS%d:%f" % (posicion, solucion[0][posicion]))
    return(solucion[0][posicion])
def read_indice(posicion):
    global indices, secuencia
    mensaje("RI%d:%f" % (posicion, indices[0][posicion]),2)
    secuencia.append("RI%d:%f" % (posicion, indices[0][posicion]))
    return(indices[0][posicion])
def read_numero(posicion):
    global numeros, secuencia
    mensaje("RN%d:%f" % (posicion, numeros[0][posicion]),2)
    secuencia.append("RN%d:%f" % (posicion, numeros[0][posicion]))
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
print("N;Real;N2;N3;N4")
for N in range(2,3):
    secuencia = []
    suma_naturales_profile(N)
    suma_naturales_check(N)
    print("%d;%d;%d;%d;%d" %(N,len(secuencia),N*N,N*N*N,N*N*N*N))
    print(secuencia)
    get_subconjuntos([1,2,3,4,5])




