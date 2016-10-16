def suma_subconjuntos(entrada):
    N = len(entrada)
    subconjuntos = 0
    for t in range(1, N+1):
        for i in range(1,N-t+2):
            sol_array=[]
            sol_sum=0
            print(i,t,check(i,t,entrada))
            subconjuntos += 1
    print("Encontrados %d subconjuntos con tamanio de entrada %d y complejidad %d %d" % (subconjuntos,N,2**(N/2),(2**(N/2))*N))
    print("%d;%d;%d;%d" % (N,subconjuntos,N**2,N**3))


def check(i,t,entrada):
    N = len(entrada)
    if t == 1:
        return(entrada[i-1])
    else:
        for j in range(i+1, N+1):
            return(entrada[i-1],check(j,t-1,entrada))



for i in range(5):
    lista=range(i*-1,i+1)
    print(lista)
    suma_subconjuntos(lista)
