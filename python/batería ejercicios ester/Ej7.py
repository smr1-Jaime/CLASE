# Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el curso actual.
#Diseñar un algoritmo para este propósito (recuerda que para calcular el porcentaje puedes hacer una regla de 3)

niños = int(input('introduzca el numero de niños: \r\n'))
niñas = int(input('introduzca el numero de niñas: \r\n'))
if niños >=0 and niñas >= 0:
    print('el porcentaje de niños es: ', end='')
    print((niños/(niños + niñas)) * 100, end='')
    print('%')

    print('el porcentaje de niñas es: ', end='')
    print((niñas/(niños + niñas)) * 100, end='')
    print('%')
else:
    print('ERROR. No puede haber un número negativo')