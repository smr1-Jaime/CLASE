#Realizar un algoritmo que lea un número por teclado. En caso de que ese número sea 0 o menor que 0,
#se saldrá del programa imprimiendo antes un mensaje de error. Si es mayor que 0, se deberá calcular su cuadrado y
#la raíz cuadrada del mismo, visualizando el número que ha tecleado el usuario y su resultado (“Del número X, su potencia es X y su raíz X”).
#Para calcular la raíz cuadrada se puede usar la función interna RAIZ(X)  o con una potencia de 0,5.

num = float(input('Introduzca el numero: \r\n'))

if num <= 0:
    print('ERROR. El numero introducido debe ser mayor que 0')
else:
    print(f'Del numero {num}, su cuadrado es ', end='')
    print(num**2)
    print('y su raiz cuadrada es ', end='')
    print(num**0.5)