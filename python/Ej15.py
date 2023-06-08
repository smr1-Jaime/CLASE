#Dada una secuencia de números leídos por teclado, que acabe con un –1, por ejemplo: 5,3,0,2,4,4,0,0,2,3,6,0,……,-1;
#Realizar el algoritmo que calcule la media aritmética. Suponemos que el usuario no insertará números negativos.
numeros = input('Introduce los números:')
numeros = numeros.split(',')
numeros = [float(numero) for numero in numeros]
media = sum(numeros) / len(numeros)

print(f'la media de los numeros es: {media}')