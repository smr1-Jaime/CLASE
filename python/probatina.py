# def leer_numeros():
#     numeros = []
    
#     while True:
#         entrada = input("Ingrese un número (0 para detenerse): ")
        
#         try:
#             numero = int(entrada)
#         except ValueError:
#             print("Entrada inválida. Intente nuevamente.")
#             continue
        
#         if numero == 0:
#             break
        
#         numeros.append(numero)
    
#     return numeros

# numeros_ingresados = leer_numeros()
# print("Números ingresados:", numeros_ingresados)

while True:
    try:
        user_input = int(input("Enter your number here: "))
        break
    except ValueError:
        pass

print(user_input)