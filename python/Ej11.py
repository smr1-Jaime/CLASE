#Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo de grado superior o no.
#Para acceder a un grado superior, si se tiene un título de bachiller, en caso de no tenerlo, se puede acceder si hemos superado una prueba de acceso.

print('Acceso a grado superior')
acceso = str.lower(input('¿Tienes titulo de bachiller? \r\n'))

if acceso == 'si':
    print('Bienvenido a grado superior')
else:
    prueba = str.lower(input('¿Superaste la prueba de acceso? \r\n'))
    if prueba == 'si':
        print('Bienvenido a grado superior')
    else:
        print('No puedes acceder a grado superior')