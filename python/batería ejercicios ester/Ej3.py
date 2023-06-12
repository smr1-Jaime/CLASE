#Algoritmo que lea dos números y nos diga cuál de ellos es mayor o bien si son iguales (recuerda usar la estructura condicional SI)

num1 = int(input('Introduzca el primer numero: \r\n'))
num2 = int(input('Introduzca el segundo numero: \r\n'))

if num1 > num2:
    print(f'el primer numero ({num1}) es mayor que el segundo ({num2})')
else:
    print(f'el segundo numero ({num2}) es mayor que el primero ({num1})')