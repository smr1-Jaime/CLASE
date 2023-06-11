#Leer tres números que denoten una fecha (día, mes, año). Comprobar que es una fecha válida.
#Si no es válida escribir un mensaje de error. Si es válida escribir la fecha cambiando el número del mes por su nombre.
#Ej. Si se introduce 1 2 2006, se deberá imprimir “1 de febrero de 2006”. El año debe ser mayor que 0.
#(Suponemos que una fecha es correcta si el día está entre 1 y 31, el mes entre 1 y 12 y el año es mayor de cero)


#Introducimos fecha y dividimos en una lista de 3 partes
fecha = input('Introduzca la fecha con el siguiente formato: 1 2 2006 \r\n')
fecha_div = fecha.split()

#La primera posición debe ser: 0<x<=31
#La segunda posición debe ser: 0<x<=12
#La tercera posición debe ser: 0<x

meses = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}

print(f'{fecha_div[0]} de {meses[int(fecha_div[1])]} de {fecha_div[2]}')