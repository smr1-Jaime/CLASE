#Se pide representar el algoritmo que nos calcule la suma de los N primeros números pares a partir de N
#(si N es par sería el primer número que hay que sumar). Es decir, si insertamos un 5, nos haga la suma de 6+8+10+12+14.
num1 = int(input('Introduzca un numero inicial: \r\n'))
num2 = int(input('Introduzca un numero final: \r\n'))
suma = 0

while num1 <= num2:
    if num1 % 2 == 0:
        suma = suma+num1
    num1 += 1
print(f'La suma es: {suma}')