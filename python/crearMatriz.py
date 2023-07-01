def CrearMatriz(M,f,c):
    for i in range(f):
        M.append([0]*c)

def IngresarMatriz(M,f,c):
    for i in range(f):
        for j in range(c):
            M[i][j] = int(input("valor: "))
def MostrarMatriz(M,f,c):
    for i in range(f):
        for j in range(c):
            print(M[i][j], end="")
        print()


M = []
f = int(input("cantidad de filas? "))
c = int(input("Cantidad de columnas? "))

CrearMatriz(M,f,c)
MostrarMatriz(M,f,c)
IngresarMatriz(M,f,c)
print("Matriz:")
MostrarMatriz(M,f,c)