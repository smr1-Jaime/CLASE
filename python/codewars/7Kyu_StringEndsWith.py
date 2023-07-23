# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples:
    # solution('abc', 'bc') # returns true
    # solution('abc', 'd') # returns false
    

def solution(text, ending):
    if ending == text[-len(ending):]:
        return(True)
    else:
        return(False)

print(solution("samurai", "ra"))

# Existe una función para comprobar el final de una cadena:     return string.endswith(ending)
