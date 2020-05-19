import numpy as np
from time import  sleep

print(f'** - Trabajo - Investigación de operaciones - **')
print("________________________________________________")
#Matriz A que contiene valores del 0 al 10
A = np.random.randint(0, 10, size=(3,3))
#Matriz B Aleatoria donde se guardará la matriz de probabilidad tomando como base la Matriz A
B = np.random.rand(3,3)

#Ciclo que crea la matriz de probabilidad por filas
for i in range(3):
    for j in range(3):
        B[i][j] = round((1/np.sum(A[i]))*A[i][j],5)

print(f'1. Matriz de probabilidad: \n{B}')

#Vector Auxiliar que contiene valores del 0 al 10
ph = np.random.randint(0, 10, size=(1,3))
#Vector Aleatorio donde se guardará el vector de probabilidad aleatorio
p0 = np.random.rand(1,3)

#Ciclo que crea el vector de probabilidad aleatorio
for item in ph:
    k = 0
    for number in item:
        p0[0][k] = round((1/np.sum(ph))*number, 2)
        k = k + 1

print(f'\nEl vector aleatorio de probabilidad es: \n{p0}')
print("________________________________________________")

print(f'3. Creación de la cadena de Markov\n')
while True:
    j = j + 1
    pk = np.dot(p0, B**j)
    pk1 = np.dot(p0, B**(j+1))
    if np.linalg.norm(pk-pk1) < 10e-8:
        break
print(f'Iteración terminada en {j}')
print(f'Norma de los vectores: {np.linalg.norm(pk-pk1)}')
print(f'Vector PK  {pk}')
print(f'Vector Pk1 {pk1}')
print("________________________________________________")

print(f'4. Calculando eig\n')
print(f'k = {j}')
#Tupla que contiene eigenvalues y eigenvectors 
w, v = np.linalg.eig(B)
print(f'Valor propio \n{np.round_(w, decimals=5)}')