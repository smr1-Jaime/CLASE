# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
# Sequence containing only one element is also considered to be strictly increasing.

def first_bad_pair(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def solution(sequence):
    j = first_bad_pair(sequence)
    if j == -1:
        return True  # Lista se incrementa
    if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True  # Eliminar elementos anteriores genera incremento
    if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True  # Eliminar elementos posteriores genera incremento 
    return False  # Eliminar elementos cualquiera no genera incremento

print(solution([1, 4, 2, 3]))