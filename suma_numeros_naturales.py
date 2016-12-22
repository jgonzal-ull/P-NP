# coding=utf-8
from variables_globales import  *
from funciones import *

def set_solucion(posicion, valor):
    global solucion, secuencia
    solucion[0][int(posicion)] = valor
    mensaje("SS%d:%f" % (posicion, valor),2)
    secuencia.append("SS%d:%f" % (posicion, valor))
def set_indice(posicion, valor):
    global indices, secuencia
    indices[0][int(posicion)] = valor
    mensaje("SI%d:%f" % (posicion, valor),2)
    secuencia.append("SI%d:%f" % (posicion, valor))
def set_numero(posicion, valor):
    global numeros, secuencia
    numeros[0][int(posicion)] = valor
    mensaje("SN%d:%f" % (posicion, valor),2)
    secuencia.append("SN%d:%f" % (posicion, valor))
def read_solucion(posicion):
    global solucion, secuencia
    mensaje("RS%d:%f" % (posicion, solucion[0][int(posicion)]),2)
    secuencia.append("RS%d:%f" % (posicion, solucion[0][int(posicion)]))
    return(solucion[0][int(posicion)])
def read_indice(posicion):
    global indices, secuencia
    mensaje("RI%d:%f" % (posicion, indices[0][posicion]),2)
    secuencia.append("RI%d:%f" % (posicion, indices[0][posicion]))
    return(indices[0][posicion])
def read_numero(posicion):
    global numeros, secuencia
    mensaje("RN%d:%f" % (posicion, numeros[0][int(posicion)]),2)
    secuencia.append("RN%d:%f" % (posicion, numeros[0][int(posicion)]))
    return(numeros[0][int(posicion)])

def suma_naturales_original(N):
    global solucion_original

    i=1
    while(i <= N):
        solucion_original[0][i - 1] = 0
        j = 1
        while(j<=i):
            solucion_original[0][i - 1] += j
            j += 1
        i += 1
def suma_naturales_profile(N):
    set_indice(0,1)  # i=1
    while(read_indice(0)<=N):  # while i<=N
        set_solucion(read_indice(0) - 1, 0)  # solucion_original[0][i - 1] = 0
        set_indice(1,1)    # j = 1
        while (read_indice(1) <= read_indice(0)): #  while(j<=i):
            set_solucion(read_indice(0)-1,read_solucion(read_indice(0)-1) + read_numero(read_indice(1))) #solucion_original[0][i - 1] += j
            set_indice(1,read_indice(1)+read_numero(1)) #j += 1
        set_indice(0,read_indice(0)+read_numero(1)) # i += 1

def suma_naturales_original_optimizado2(N):
    global solucion_original

    solucion_original[0][0] = 1
    i=2
    while( i <= N ):
        solucion_original[0][i - 1] = solucion_original[0][i - 2] + i
        i += 1
def suma_naturales_profile_optimizado2(N):
    set_solucion(0,read_numero(1))  # solucion_original[0][0] = 1

    set_indice(0,2)  # i=2
    while(read_indice(0)<=N):  # while i<=N
        set_solucion(read_indice(0) - 1, read_solucion(read_indice(0)-2) + read_numero(read_indice(0)))  # solucion_original[0][i - 1] = 0
        set_indice(0,read_indice(0)+read_numero(1)) # i += 1


def suma_naturales_original_optimizado1(N):
    global solucion_original

    i=1
    while(i <= N):
        suma = 0
        j = 1
        while(j<=i):
            suma += j
            j += 1
        solucion_original[0][i - 1] = suma
        i += 1
def suma_naturales_profile_optimizado1(N):
    set_indice(0,1)  # i=1
    while(read_indice(0)<=N):  # while i<=N
        set_indice(2, 0)  # suma = 0
        set_indice(1,1)    # j = 1
        while (read_indice(1) <= read_indice(0)): #  while(j<=i):
            set_indice(2, read_indice(2)+read_numero(read_indice(1))) # suma += j
            set_indice(1,read_indice(1)+read_numero(1)) #j += 1
        set_solucion(read_indice(0)-1,read_indice(2)) #solucion_original[0][i - 1] = suma
        set_indice(0,read_indice(0)+read_numero(1)) # i += 1

def suma_naturales_check(N):
    global solucion, solucion_original
#    print(solucion)
#    print(solucion_original)
#    print(solucion == solucion_original)
    return(solucion == solucion_original)


print("N;Longitud Secuencia;Conjuntos Posibles;Conjuntos Diferentes;N2;N3;N4")
for N in range(2,20):
    secuencia = []
#    suma_naturales_original(N)
#    suma_naturales_profile(N)
#    suma_naturales_original_optimizado1(N)
#    suma_naturales_profile_optimizado1(N)
    suma_naturales_original_optimizado2(N)
    suma_naturales_profile_optimizado2(N)
    if np.all(suma_naturales_check(N)[0]):
        mensaje("%d;%d;%d;%d;%d;%d;%d" %(N,len(secuencia),get_subconjuntos(secuencia), \
                                        get_subconjuntos_diferentes(secuencia), \
                                         N*N,N*N*N,N*N*N*N, \
                                        ),0)


