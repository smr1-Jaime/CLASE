#Calcula las siguientes sumas de números codificados con 8 bits en el sistema posicional:
#a) 01111111 + 00000001
#b) 01010101 + 10101010
#c) 00000011 + 00000001

a1 = int("01111111", 2)
a2 = int("00000001", 2)
solucionA = bin(a1 + a2)

b1 = int("01010101", 2)
b2 = int("10101010", 2)
solucionB = bin(b1 + b2)

c1 = int("00000011", 2)
c2 = int("00000001", 2)
solucionC = bin(c1 + c2)


print(f'01111111 + 00000001 = {solucionA[2:len(solucionA)]}')
print(f'01010101 + 10101010 = {solucionB[2:len(solucionB)]}')
print(f'00000011 + 00000001 = {solucionC[2:len(solucionC)]}')