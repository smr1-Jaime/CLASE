# Cambio de variable sencillo
def cambio_variable():
    a = 1
    b = 2
    a,b = b,a
    return(a, b)

# Invertir cadena de texto
def cadena_invertida():
    cadena = "hola que tal"
    return(cadena[::-1])

# Unir elementos de lista
def unir_palabras():
    palabras = ["hola", "que", "tal"]
    return(" ".join(palabras))

# Iniciar una lista con un mismo valor repetido
def lista_valor_repetido():
    lista = [100]*20
    return(lista)

# Mezclar dos diccionarios
def mezclar_diccionarios():
    diccionario = {"nombre":"pepe", "edad":25}
    diccionario2 = {"estado":"soltero", "estudios":"derecho y sentado"}
    d3 = {**diccionario, **diccionario2}
    return(d3)

print(mezclar_diccionarios())