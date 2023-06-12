#Calcular el número de divisores de un número, mayor o igual que la unidad.

numero = int(input('Introduzca un numero igual o mayor que 1: \r\n'))

if numero >= 1:
    
    divisores = 0
    print (f'Los divisores de {numero}:')
    for divisor in range(1, numero + 1):
        if (numero % divisor) == 0:
            print(f'{divisor} es divisor')
            divisores += 1
    
else:
    print(f'ERROR. {numero} no es mayor o igual que 1')