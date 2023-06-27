def solution(inputString):
    inicio = 0
    fin = -1
    palindromo = True

    while abs(fin) <= len(inputString):
        if inputString[inicio] != inputString[fin]:
            palindromo = False
            break
        inicio += 1
        fin -= 1
    return(palindromo)

solution('aabaa')

