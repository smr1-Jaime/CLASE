#Algoritmo que lea números enteros hasta teclear 0, y nos muestre el máximo, el mínimo y la media de todos ellos.
#Piensa como debemos inicializar las variables.

numeros = []

preguntar = True

while preguntar:
    respuesta = int(input('Introduzca un numero: \r\n'))
    numeros.append(respuesta)
    if respuesta == 0:
        preguntar = False

numeros.remove(0)

maximo = max(numeros)
minimo = min(numeros)
media = sum(numeros) / len(numeros)

print(f'El mayor de los numeros es: {maximo}')
print(f'El minimo de los numeros es: {minimo}')
print(f'La media de los numeros es: {media}')