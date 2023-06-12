#Realizar la tabla de multiplicar de un número entre 0 y 10.

numero = int(input(' Introduzca un numero entre 0 y 10: \r\n'))
tabla = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

if numero <=10 and numero >=0:
    for i in tabla:
        print(f'{numero} × {i} = {numero * i}')
else:
    print('ERROR. El numero no está entre 0 y 10')
    