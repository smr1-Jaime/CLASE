#Pedir un número en formato decimal y mostrar dicho número en octal.

numero = int(input('Introduzca un numero: \r\n'))
numero = (oct(numero))

print(numero[2:len(numero)])