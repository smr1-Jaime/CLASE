#Imprimir y contar los números que son múltiplos de 2 o de 3 que hay entre 1 y 100.
contador = 0
for i in range(1, 101):
    if i % 2 == 0 or i % 3 == 0:
        print(i)
        contador +=1
        
print(f'El total de numeros multiplos de 2 o 3 es: {contador}')
