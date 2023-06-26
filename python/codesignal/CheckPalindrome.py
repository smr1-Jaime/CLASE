#Given the string, check if it is a palindrome.

# def solution(inputString):
cadena = input()    
    
inicio = 0
fin = len(cadena) - 1
while cadena[inicio] == cadena[fin]:
    if inicio >= fin:
        palindromo = True
    inicio += 1
    fin -= 1
palindromo = False

print(palindromo)

# solution('aabaa')