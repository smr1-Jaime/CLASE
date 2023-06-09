numeros = [2, 5, 8, 0, 3, 1, 0]
valor = 0

if valor in numeros:
    posicion = numeros.index(valor)
    print(f"El valor {valor} se encuentra en la posición {posicion} de la lista.")
else:
    print(f"El valor {valor} no está presente en la lista.")

print(type(numeros))



# numeros = [2, 5, 8, 0, 3, 1, 0, 7, 0]
# valor = 0
# posiciones = []

# for i in range(len(numeros)):
#     if numeros[i] == valor:
#         posiciones.append(i)

# if posiciones:
#     print(f"El valor {valor} se encuentra en las posiciones:")
#     for posicion in posiciones:
#         print(posicion)
# else:
#     print(f"El valor {valor} no está presente en la lista.")