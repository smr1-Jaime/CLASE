#Se pide representar el algoritmo que nos calcule la suma de los N primeros números naturales.
#N se leerá por teclado (no tenemos porqué llamar a la variable N, podemos llamarla como queramos).
numero = int(input('Introduzca un numero: \r\n'))
numeros = range(1, numero + 1)
print(f'La suma del rango del 0 al {numero} es: {sum(numeros)}')
