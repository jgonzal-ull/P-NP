from time import time
llamadas = {}
verbose = 0



lista = []
sol_actual = []
sol_suma = 0
N = 0
subconjuntos_totales = 0
subconjuntos_correctos = 0

valores_llamadas = {}
sumas_llamadas = {}
indices_menos_uno = {}
ind_actual = 0

def mensaje(cadena):
    global verbose

    if verbose == 1:
        print(cadena)
#@profile
def suma_subconjuntos_exponencial():
    global lista, sol_actual, sol_suma, N, subconjuntos_totales, subconjuntos_correctos, verbose

    global llamadas, valores_llamadas, sumas_llamadas, ind_actual

    subconjuntos_totales = 0
    subconjuntos_correctos = 0
    llamadas = {}
    valores_llamadas = {}
    sumas_llamadas = {}
    for t in range(1, N + 1):
        for i in range(N-t+1):
            sol_actual = [lista[i]]
            sol_suma=lista[i]
            check_exponencial(i,t)

def suma_subconjuntos_polinomial():
    global lista, sol_actual, sol_suma, N, subconjuntos_totales, subconjuntos_correctos, verbose

    global llamadas, valores_llamadas, sumas_llamadas, ind_actual, indices_menos_uno

    subconjuntos_totales = 0
    subconjuntos_correctos = 0
    llamadas = {}
    valores_llamadas = {}
    sumas_llamadas = {}
    for i in range(N):
        ind_actual = 2**i
        valores_llamadas[ind_actual]=[lista[i]]
        sumas_llamadas[ind_actual]=lista[i]
        indices_menos_uno[i] = ind_actual
    for t in range(2, N + 1):
        for i in range(N - t + 1):
            for j in range(i + 1, N):
                ind_actual = 2**i + indices_menos_uno[j]
                valores_llamadas[ind_actual] = [lista[i]] + [x for x in valores_llamadas[indices_menos_uno[j]]]
                sumas_llamadas[ind_actual] = lista[i] + sumas_llamadas[indices_menos_uno[j]]
                indices_menos_uno[j] = ind_actual


#@profile
def check_exponencial(i,t):
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
            check_exponencial(j,t-1)
            sol_actual = sol_actual[:-1]
            sol_suma -= lista[j]

for i in range(3,4):
    lista=range(i*-1,i+1)
    mensaje("Comenzando problema: ")
    N = len(lista)
    tiempo_inicial = time()
    suma_subconjuntos_polinomial()
    tiempo_final = time()
    tiempo = tiempo_final - tiempo_inicial
    print("N = %d; Subconjuntos_totales = %d;Subconjuntos_correctos = %d; Tiempo = %f; llamadas_diferentes = %d" % (N, subconjuntos_totales, subconjuntos_correctos, tiempo, len(llamadas)))
    mensaje("Analizados %d subconjuntos (%d buenos) con tamanio de entrada %d" % (subconjuntos_totales, subconjuntos_correctos, N))





