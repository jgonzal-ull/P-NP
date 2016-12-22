import numpy as np

Nnum = 100

solucion = np.zeros((1, Nnum))
solucion_original = np.zeros((1, Nnum))
solucion_original_profile = np.zeros((1, Nnum))
numeros = np.zeros((1,Nnum))
indices = np.zeros((1,Nnum))
secuencia=[]

for i in range(0,Nnum):
    numeros[0][i] = i
