#CREACION DE MATRIZ DE 3X3

matriz=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
#ACCESO A LOS ALEMENTOS: MATRIZ[FILA][COLUMA]
print(matriz[1][2])#fila indie 1, columna indice 2
#NODIFICAR ELEMENTOS
matriz[0][0] = 100
#RECORRER LA MATRIZ
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()   





#CREACION DE MATRICES
A = [[1,2]],[[3,4]]
B = [[5,6]],[[7,8]]

suma = [[A[i][j] +B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print (suma)