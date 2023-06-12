#Algoritmo que lea tres números distintos y nos diga cuál de ellos es el mayor (recuerda usar la estructura condicional Si y los operadores lógicos)

num1 = int(input('introduzca el primer numero: \r\n'))
num2 = int(input('introduzca el segundo numero: \r\n'))
num3 = int(input('introduzca el tercer numero: \r\n'))

if num1 > num2 and num1 > num3:
    print(f'el primer numero ({num1}) es mayor que el segundo ({num2}) y el tercero ({num3})')
else:
    if num2 > num1 and num2 > num3:
        print(f'el segundo numero ({num2}) es mayor que el primero ({num1}) y el tercero ({num3})')
    else:
        if num3 > num1 and num3 > num2:
            print(f'el tercer numero ({num3}) es mayor que el primero ({num1}) y el segundo ({num2})')