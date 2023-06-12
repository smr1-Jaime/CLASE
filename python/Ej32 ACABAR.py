#Dado un número que se pedirá al usuario y que estará entre 1 y 4000. Pasarlo a números romanos y mostrarlo.

romanos = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
naturales = [1000, 500, 100, 50, 10, 5 , 1]


numero = int(input('Introduzca un numero entre 1 y 4000: \r\n'))
if numero >=1 and numero <= 4000:
    print('Está dentro del rango')
else:
    print(f'ERROR. El número {numero} no esta entre 1 y 4000')