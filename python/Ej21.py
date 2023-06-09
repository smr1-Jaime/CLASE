#Hacer un pseudocódigo que imprima los números del 1 al 100.
#Que calcule la suma de todos los números pares por un lado, y por otro, la de todos los impares.

for numero in range(1, 101):
    print(numero)


def sumaParesImpares(num1, num2, pares):
    suma = 0
    for i in range(num1, num2 +1):
        if pares == True and i % 2 == 0:
            suma = suma + i
        else:
            if pares == False and i % 2 != 0:
                suma = suma + i
    return(suma)

suma_pares = sumaParesImpares(1, 100, True)
print(f'La suma de los números pares es: {suma_pares}')

suma_impares = sumaParesImpares(1, 100, False)
print(f'La suma de los números impares es: {suma_impares}')

# num = int(input('Introduzca un numero: \r\n'))

# if num % 2 == 0:
#     print(f'el numero {num} es par')
# else:
#     print(f'el numero {num} es impar')