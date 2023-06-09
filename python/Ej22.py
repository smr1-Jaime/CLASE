#Imprimir y contar los números que son múltiplos de 2 o de 3 que hay entre 1 y 100.
def contador():
    for i in range(1, 101):
        if i % 2 == 0 or i % 3 == 0:
            lista = i
            print(lista)
