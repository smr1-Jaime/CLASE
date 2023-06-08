#Calcular las calificaciones de un grupo de alumnos. La nota final de cada alumno se calcula según el siguiente criterio:
#la parte práctica vale el 10%; la parte de problemas vale el 50% y la parte teórica el 40%. El algoritmo leerá el nombre del alumno,
#las tres notas, escribirá el resultado y volverá a pedir los datos del siguiente alumno hasta que el nombre sea una cadena vacía.
#Las notas deben estar entre 0 y 10, si no lo están, no imprimirá las notas, mostrará un mensaje de error y volverá a pedir otro alumno.

alumno = input('Introduzca el nombre del alumno: \r\n')
practica = int(input('Introduzca la nota práctica: \r\n'))
problemas = int(input('Introduzca la nota de los problemas: \r\n'))
teorica = int(input('Introduzca la nota teórica: \r\n'))

practica = practica * 0.1
problemas = problemas * 0.5
teorica = teorica * 0.4

notas = alumno + practica + problemas, teorica
print(notas)