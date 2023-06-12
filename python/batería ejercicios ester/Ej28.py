#Pedir un número en formato decimal y mostrar dicho número en binario.

numero = int(input('Introduzca un numero: \r\n'))
numero = (bin(numero))

print(numero[2:len(numero)])