#Dado un número que se pedirá al usuario y que estará entre 1 y 4000. Pasarlo a números romanos y mostrarlo.

def convertir_a_romano(numero):
    simbolos = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    
    numero_romano=''
    for valor, simbolo in simbolos.items():
        while numero >= valor:
            numero_romano += simbolo
            numero -= valor
    
    return numero_romano

numero_natural = int(input('Introduzca un numero natural: \r\n'))

if numero_natural <= 4000:
    numero_romano = convertir_a_romano(numero_natural)
    print(f'El numero {numero_natural} en numeros romanos es: {numero_romano}')
else:
    print('ERROR. El numero debe estar entre 1 y 4000')