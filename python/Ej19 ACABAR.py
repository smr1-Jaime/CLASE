#Leer tres números que denoten una fecha (día, mes, año). Comprobar que es una fecha válida.
#Si no es válida escribir un mensaje de error. Si es válida escribir la fecha cambiando el número del mes por su nombre.
#Ej. Si se introduce 1 2 2006, se deberá imprimir “1 de febrero de 2006”. El año debe ser mayor que 0.
#(Suponemos que una fecha es correcta si el día está entre 1 y 31, el mes entre 1 y 12 y el año es mayor de cero)

fecha = input('Introduzca la fecha con el siguiente formato: 1 2 2006 \r\n')
fecha_div = fecha.split()

print(fecha_div)































# fecha = (input('Introduzca una fecha: \r\n'))
# numeros = fecha.split()
# print(numeros)
# print(type(numeros))

# contador = 0

# while contador < 3:
#     try:
#         user_input = int(input("Introduzca la fecha: \r\n"))
#         contador += 1
#         user_input += user_input
#     except ValueError:
#         pass

# print(user_input)
