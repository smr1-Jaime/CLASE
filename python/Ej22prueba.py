# def es_multiplo(numeros, multiplo):
#     return numeros % multiplo == 0

# imprimir = es_multiplo(range(1, 101), 2)

# print (imprimir)

for i in range(1, 101):
   if i % 2 == 0 or i % 3 == 0:
      print(i)