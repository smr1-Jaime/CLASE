# Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo, debe imprimir el producto de los tres y si no lo es, imprimirá la suma.

num1 = int(input('introduzca el primer numero: \r\n'))
num2 = int(input('introduzca el segundo numero: \r\n'))
num3 = int(input('introduzca el tercer numero: \r\n'))

if num1 < 0:
    print('el resultado es: ', end='')
    print(num1 * num2 * num3)
else:
    print('el resultado es: ', end='')
    print(num1 + num2 + num3)