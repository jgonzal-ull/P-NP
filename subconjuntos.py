def suma_subconjuntos(entrada):
    N = len(entrada)
    subconjuntos = 0
    for t in range(1, N+1):
        for i in range(1,N-t+2):
#            print(i,t,check(i,t,entrada))
            subconjuntos += 1
#    print("Encontrados %d subconjuntos con tamanio de entrada %d y complejidad %d %d" % (subconjuntos,N,2**(N/2),(2**(N/2))*N))
    print("%d;%d;%d;%d" % (N,subconjuntos,N**2,N**3))


def check(i,t,entrada):
    N = len(entrada)
    if t == 1:
        return(entrada[i-1])
    else:
        for j in range(i+1, N+1):
            return(entrada[i-1],check(j,t-1,entrada))


lista = []
for i in range(1,3000):
    lista.append(i)
    suma_subconjuntos(lista)
