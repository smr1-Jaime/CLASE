#Algoritmo que lea números enteros hasta teclear 0, y nos muestre el máximo, el mínimo y la media de todos ellos.
#Piensa como debemos inicializar las variables.

numeros = input('Introduzca numeros:')
numeros_div = numeros.split()
numeros = [float(numero) for numero in numeros_div]

valor = 0

maximo = max(numeros)
minimo = min(numeros)
media = sum(numeros) / len(numeros)

def imprimir():
    print(maximo)
    print(minimo)
    print(media)


if valor in numeros_div:
    posicion = numeros_div.index(valor)
    print(numeros_div)
print(numeros_div)









# for (posicion = 0) in (posicion < len(numeros_div)):
#     posicion += 1
#     if numeros_div[posicion] = 0:
#     break

