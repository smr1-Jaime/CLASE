#Modificar el algoritmo anterior, de forma que si se teclea un cero, se vuelva a pedir el número por teclado
#(así hasta que se teclee un número mayor que cero) (recuerda la estructura mientras).

preguntar = True

while preguntar == True:
    respuesta = int(input('Introduzca un numero: \r\n'))
    if respuesta == 0:
         print('El numero es 0')
         preguntar = False
    elif respuesta % 2 == 0:
        print(f'el numero {respuesta} es par')
    elif respuesta % 2 == 1:
        print(f'el numero {respuesta} es impar')