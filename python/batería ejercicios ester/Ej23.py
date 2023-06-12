#Hacer un pseudocódigo que imprima el mayor y el menor de una serie de cinco números que vamos introduciendo por teclado.

numeros = input('Introduzca 5 números: \r\n')
numeros = numeros.split()

maximo = max(numeros)
menor = min(numeros)

if len(numeros) != 5:
    print('ERROR. La cantidad de números ha de ser 5')
else:
    print(f'El número mayor de los intoducidos es: {maximo}')
    print(f'El número menor de los intoducidos es: {menor}')