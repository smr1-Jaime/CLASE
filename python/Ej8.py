#Una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes de octubre.
#Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar al cliente.

mes = str.lower(input('Introduzca el mes en el que se realiza la compra: \r\n'))
importe = float(input('Introduzca el importe de la compra \r\n'))

if mes == "octubre":
    print('el importe total es: ', end='')
    importe_oct = importe - (importe * 0.15)
    float_str = str(importe_oct)
    print(f'el importe total es: {float_str}€')
else:
    print(f'el importe total es: {importe}€')
