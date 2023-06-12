#Codifica en complemento a dos de 8 bits los siguientes valores:
#a) 4 b) −4 c) 0 d) 127 e) 1 f) −1

numeros = {4, -4, 0, 127, 1, -1}

def complemento(x):
    x = str(x)
    new_bin = x.replace('1', 'a')
    new_bin = new_bin.replace('0', '1')
    new_bin = new_bin.replace('a', '0')
    return new_bin

for numero in numeros:
    binario = bin(numero)
    # print(f'{numero} en binario es: {binario}') 
    numeros = list(binario)
    # print(binario)
    print(complemento(binario))

