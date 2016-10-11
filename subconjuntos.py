def suma_subconjuntos(entrada):
    N = len(entrada)
    for t in range(1, N+1):
        for i in range(1,N-t+2):
            print(i,t,check(i,t,entrada))

def check(i,t,entrada):
    N = len(entrada)
    if t == 1:
        return(entrada[i-1])
    else:
        for j in range(i+1, N+1):
            return(entrada[i-1],check(j,t-1,entrada))

suma_subconjuntos([-2, -1, 0, 1, 2])
