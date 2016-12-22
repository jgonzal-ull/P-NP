# coding=utf-8

verbose = 0

# 0 Sólo errores graves de funcionamiento
# 1 Errores y mensajes resumidos detalle medio
# 2 Detalle máximo
def mensaje(cadena, nivel):
    global verbose
    if nivel <= verbose:
        print(cadena)


def get_subconjuntos(conjunto):
    longitud = len(conjunto)
    conjuntos = 0
    for long in range(1,longitud+1):  #logitudes de los conjuntos
        for pos in range(0,longitud-long+1): #primer campo del conjunto
#            print("Longitud: %d    Posición: %d" % (long, pos))
            elemento=[]
            for pref in range(pos, pos+long):
                elemento.append(conjunto[pref])
            conjuntos += 1
#            print(elemento)
    return(conjuntos)

def get_subconjuntos_diferentes(conjunto):
    conj = set(conjunto)
    conjuntos_diferentes = len(conj)
    return (conjuntos_diferentes)
