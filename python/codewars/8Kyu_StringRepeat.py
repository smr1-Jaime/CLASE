# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    all = ''
    for i in range(0,repeat):
        all += string
    return(all)
    # return(repeat*string) Solución más óptima de la que me di cuenta después

print(repeat_str(5,'hola'))