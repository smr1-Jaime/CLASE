#Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size.
#Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1.
#He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
def solution(statues):
    ordenado = sorted(statues)

    primero = ordenado[0]
    ultimo = ordenado[-1]

    numeros = []
    escribir = True

    while escribir:
        for n in range(primero, ultimo+1):
            numeros.append(n)
        escribir = False

    long_statues = len(statues)
    long_numeros = len(numeros)

    return(long_numeros - long_statues)

print(solution([1, 5, 9, 1234]))