#¿Cuántos bits se necesitan para representar los números del 0 al 18, ambos inclusive?
numero = bin(18)
binario = numero[2:len(numero)]
print(f'La longitud necesaria para representar los numeros del 0 al 18 es: {len(binario)}')