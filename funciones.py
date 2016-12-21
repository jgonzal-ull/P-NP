# coding=utf-8

def get_subconjuntos(conjunto):
    longitud = len(conjunto)
    for long in range(1,longitud+1):  #logitudes de los conjuntos
        for pos in range(0,longitud-long+1): #primer campo del conjunto
            print("Longitud: %d    Posición: %d" % (long, pos))
            elemento=[]
            for pref in range(pos, pos+long-1):
                elemento.append(conjunto[pref])
            for sig in range(pos+long-1,longitud):
                elemento.append(conjunto[sig])
                print(elemento)
                elemento.pop()


