#Pedir un número en formato decimal y mostrar dicho número en hexadecimal.

numero = int(input('Introduzca un numero: \r\n'))
numero = (hex(numero))

print(numero[2:len(numero)])