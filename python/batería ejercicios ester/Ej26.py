#Comprobar si un número, mayor o igual que la unidad, es primo.

numero = int(input('Introduzca un numero: \r\n'))

if numero >= 1:
    divisores = 0
    for divisor in range(1, numero + 1):
        if (numero % divisor) == 0:
            divisores += 1
    if divisores == 2:
        print(f'{numero} es primo')
    else:
        print(f'{numero} no es primo')
else:
    print(f'ERROR. El numero introducido debe ser mayor o igual que 1')
