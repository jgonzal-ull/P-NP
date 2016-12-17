from time import time
llamadas = {}
verbose = 0


solucion = []


def mensaje(cadena, nivel):
    global verbose
    if nivel <= verbose:
        print(cadena)

def suma_naturales_original(N):
    global solucion

    for i in range(1,N):
        solucion[i] = 0
        for j in range(1,i):
            solucion[i] += j





suma_naturales_original(10)
print(solucion)






