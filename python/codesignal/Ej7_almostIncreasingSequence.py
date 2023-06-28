# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
# Sequence containing only one element is also considered to be strictly increasing.

def solution(sequence):
    contador = 0
    numero = 0
    tamaño = len(sequence)
    if sequence[0] > sequence[1]:
        sequence.pop(0)
        contador +=1
        tamaño -=1
    while numero < tamaño -1:
        if sequence[numero] >= numero + 1:
            contador += 1
            if sequence[numero + 1] <= sequence[numero - 1]:
                sequence.pop(numero + 1)
            else:
                sequence.pop(numero)
            tamaño = len(sequence)
            if numero > 0:
                numero -= 1
        else:
            numero + 1
    if contador > 1:
        return False
    else:
        return True
    
print(solution([1, 2, 1]))