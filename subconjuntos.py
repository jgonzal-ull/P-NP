from time import time
llamadas = {}
verbose = 0

@profile

lista = []
sol_actual = []
sol_suma = 0
N = 0
subconjuntos_totales = 0
subconjuntos_correctos = 0



def mensaje(cadena):
    global verbose

    if verbose == 1:
        print(cadena)

def suma_subconjuntos():
    global lista, sol_actual, sol_suma, N, subconjuntos_totales, subconjuntos_correctos, verbose

    global llamadas

    subconjuntos_totales = 0
    subconjuntos_correctos = 0
    llamadas = {}
    for t in range(1, N + 1):
        for i in range(N-t+1):
            sol_actual = [lista[i]]
            sol_suma=lista[i]
            check(i,t)

def check(i,t):
    global lista, sol_actual, sol_suma, N, subconjuntos_totales, subconjuntos_correctos, verbose

    global llamadas

    if llamadas.has_key(i*100+t):
        llamadas[i*100+t] += 1
    else:
        llamadas[i*100+t] = 1
    if t == 1:
        if sol_suma == 0:
            mensaje("CORRECTO")
            mensaje(sol_actual)
            subconjuntos_correctos += 1
            subconjuntos_totales += 1
        else:
            mensaje(sol_actual)
            subconjuntos_totales += 1
    else:
        for j in range(i+1, N):
            sol_actual.append(lista[j])
            sol_suma += lista[j]
            check(j,t-1)
            sol_actual = sol_actual[:-1]
            sol_suma -= lista[j]


for i in range(2,10):
    lista=range(i*-1,i+1)
    mensaje("Comenzando problema: ")
    N = len(lista)
    tiempo_inicial = time()
    suma_subconjuntos()
    tiempo_final = time()
    tiempo = tiempo_final - tiempo_inicial
    print("%d;%d;%d;%f;%d" % (N, subconjuntos_totales, subconjuntos_correctos, tiempo, len(llamadas)))
    mensaje("Analizados %d subconjuntos (%d buenos) con tamanio de entrada %d" % (subconjuntos_totales, subconjuntos_correctos, N))




