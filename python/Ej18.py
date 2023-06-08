#Algoritmo que pida un año y compruebe si es bisiesto. Un año es bisiesto si es divisible para 4 y no lo es para 100 o si es divisible para 400.

año = int(input('Introduzca un año: \r\n'))
 
if año % 4  == 0 and año % 100  != 0 or año % 400 == 0:
    print(f'El año {año} es bisiesto')
else:
    print(f'El año {año} no es bisiesto')