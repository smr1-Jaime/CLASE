// Dadas dos variables numéricas A y B, que el usuario debe teclear,
//se pide realizar un algoritmo que intercambie los valores de ambas variables
//y muestre cuánto valen al final las dos variables (recuerda la asignación).

num1 = prompt('Introduzca el primer numero:')
num2 = prompt('Introduzca el segundo numero:')

numAux1 = num2
numAux2 = num1

num1 = numAux1
num2 = numAux2

print('El valor del primer numero es: ') + num1
print('El valor del segundo numero es: ') + num2