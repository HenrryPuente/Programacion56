import random
print("ingrese el numero de filas")
n=int(input())
print("ingrese el numero de columnas")
m=int(input())

matriz = []

for i in range(n):
    matriz.append([])
    for j in range(m):
        matriz[i].append(random.randint(0, 100))
for k in matriz:
    print (k)
print("DIAGONAL PRINCIPAL")
a=[]
for i in range(n):
    a.append(matriz[i][i])
print(a)
print("DIAGONAL SECUNDARIA")
b=[]
for i in range(n):
    b.append(matriz[i][(m-1)-i])
print(b)
