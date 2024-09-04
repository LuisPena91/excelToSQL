import numpy as np

# Crear una matriz 3x3
matriz_np = np.empty((5,5))

x = 1
for i in range(5):
    for j in range(5):
        matriz_np[i,j] = x
        x+=1

# Imprimir la matriz
print(matriz_np[0][4])
        