#Realizar un algoritmo que dado un número entero, visualice en pantalla si es par o impar.

num = int(input('Introduzca un numero: \r\n'))

if num % 2 == 0:
    print(f'el numero {num} es par')
else:
    print(f'el numero {num} es impar')