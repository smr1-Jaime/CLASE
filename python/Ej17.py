#Algoritmo que lea números enteros hasta teclear 0, y nos muestre el máximo, el mínimo y la media de todos ellos.
#Piensa como debemos inicializar las variables.

numeros = input('Introduzca numeros:')
numeros_div = numeros.split()
numeros = [float(numero) for numero in numeros_div]

maximo = max(numeros)
minimo = min(numeros)
media = sum(numeros) / len(numeros)

print(maximo)
print(minimo)
print(media)