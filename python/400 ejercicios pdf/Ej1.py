#¿Cual es el maximo valor que puede representarse con 16 bits y un sistema de representación posicional como el descrito?
#¿Que secuencia de bits le corresponde? //binario

total = (2**17) - 1 #131071
secuencia = bin(total)
print(secuencia[2:len(secuencia)])
