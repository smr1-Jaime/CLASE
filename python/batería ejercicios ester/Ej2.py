#Algoritmo que lea dos números, calculando y escribiendo el valor de su suma, resta, producto y división.

num1 = int(input('Introduzca el primer numero: \r\n'))
num2 = int(input('Introduzca el segundo numero: \r\n'))

operaciones = ['la suma es:', 'la resta es:', 'el producto es:', 'la division es:']
resultados = [num1 + num2, num1 - num2, num1 * num2, num1 / num2]

for operacion, resultado in zip(operaciones, resultados):
    print(operacion, resultado)