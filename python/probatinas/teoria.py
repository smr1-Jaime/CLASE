#variables
#nombre = "juan"
#likes = 201
#total_pagar = 100.20
#pagado = True
#print(nombre, likes, total_pagar, pagado)
#-------------------------------------------------------
#-------------------------------------------------------
#funciones

#definir funcion
#def informacion (nombre, puesto = 'desconocido'):
#    print(f'soy {nombre} y soy {puesto}')
#llamar funcion
#informacion('Pedro', 'Programador')
#informacion('Itzel',)
#-------------------------------------------------------
#metodos
#def informacion(nombre):
#    return nombre
#
#empleado = informacion('Juan')
#print (empleado)
#-------------------------------------------------------
#nombre = 'pedro'

#def mostrar_nombre(nombre):
#    print (f'Hola {nombre}')

#mostrar_nombre(nombre)

#print( nombre.upper() )
#print( nombre.title() )
#-------------------------------------------------------
# def bienvenida():
#     print ('Bienvenido a python')
# bienvenida()

# def bienvenida_usuario(nombre):
#     print(f'Bienvenido a python {nombre}')
# bienvenida_usuario('Jaime')

# def ultima_actividad():
#     print ("mi ultima actividad fue ver un video")
# ultima_actividad
#-------------------------------------------------------
#-------------------------------------------------------
#NUMEROS#
# print(2)
# print(4)

# print(2.5)

# print (2 + 3)
# print (8 - 4)
# print (1 * 4)
# print (10 / 3)
# print (4 ** 3)
# print ( (2 + 3) * 4)

# numero = 20
# print (numero)
# numero += 1
# print(numero)

# print(4 + 2.9)
#-------------------------------------------------------
# def suma (a = 0, b = 0):
#     print(a + b)
# suma ( 2, 3 )
# suma ( 4, 1 )
# suma ( 8,  )

# def resta(a = 0, b = 0):
#     print (a - b)
# resta(10, 8)

# def multiplicacion(a = 0, b = 0):
#     print(a * b)
# multiplicacion(4, 9)

# def division(a = 0, b = 1):
#     print (a / b)
# division (10, 3)
#-------------------------------------------------------
#ARRAYS o ARREGLOS
# meses = ["enero", "febrero", "marzo"]
# print(meses[0])
#-------------------------------------------------------
# lenguajes = ['python', 'kotlin', 'java', 'javascript']
# print (lenguajes)

# #siempre se comienza en 0
# print(lenguajes[0])

# #ordenar elementos
# lenguajes.sort()
# print(lenguajes)

# #acceder a un elemento dentro de un texto
# aprendiendo = f'estoy aprendiendo {lenguajes[3]}'
# print(aprendiendo)

# #modificar valores de un arreglo
# lenguajes[2] = 'PHP'
# print(lenguajes)

# #agregar elementos a un arreglo
# lenguajes.append('Ruby')
# print(lenguajes)

# #eliminar elemento de un arreglo
# del lenguajes[1]
# print(lenguajes)

# #eliminar de un arreglo
# lenguajes.pop() #elimina el último elemento
# print(lenguajes)

# #eliminar con pop una posición concreta
# lenguajes.pop(0)
# print(lenguajes)

# #eliminar por nombre
# lenguajes.remove('PHP')
# print(lenguajes)
#-------------------------------------------------------
#-------------------------------------------------------
# #ITERADORES
# lenguajes = ['python', 'kotlin', 'java', 'javascript', 'PHP', 'Ruby', 'GO']

# #iterador
# for lenguaje in lenguajes:
#     print(f'Estoy aprendiendo {lenguaje}')

# #for que escriba numeros
# for numero in range(0, 20):
#     print(numero)
#-------------------------------------------------------
#-------------------------------------------------------
#CONDICIONALES
# balance = 500

# if balance > 501:
#     print("puedes pagar")
# else:
#     print('No tienes saldo')
#---operadores---
# operadores = ["==", "!=", ">", ">=", "<", "<=" ]
# significados = ["igual a", "diferente a", "mayor a", "mayor o igual a", "menor a", "menor o igual a"]

# for operador, significado in zip(operadores, significados): # zip une varios iterables y cada unión de estos crea una dupla
#     print(f'{operador} es {significado}')

#if con nums
# likes = 200
# if likes >= 200:
#     print('Excelente, 200 likes')
# else:
#     print('casi llegas a los 200')

# #if con texto
# lenguaje = 'python'
# if not lenguaje == 'PHP':
#     print('Excelente decisión')

# #evaluar boolean
# usuario_autenticado = True
# if usuario_autenticado == True:
#     print('Acceso al sistema')
# else:
#     print('debes iniciar sesión')
#-------------------------------------------------------
#evaluar elemento de una lista
# lenguajes = ['python', 'kotlin', 'java', 'javascript', 'PHP', 'Ruby', 'GO']
# if 'PHP' in lenguajes:
#     print('PHP si existe')
# else:
#     print('No esta en la lista')

# #if anidados
# usuario_autenticado = True
# usuario_admin = True

# if usuario_autenticado:
#     if usuario_admin:
#         print('acceso total')
#     else:
#         print('acceso al sistema')
# else:
#     print('debes iniciar sesion')

# #elif
# ocupacion = 'nada'
# if ocupacion == 'estudiante':
#     print('tienes 50% de descuento')
# elif ocupacion == 'jubilado':
#     print('tienes 75% de descuento')
# elif ocupacion == 'desempleado':
#     print('tienes un 10% de descuento')
# else:
#     print('debes pagar el 100%')
#-------------------------------------------------------
#operadores and y or
# usuario_logueado = True
# usuario_admin = True
# if usuario_logueado or usuario_admin:
#     print('administrador')
# elif usuario_logueado:
#     print('acceso al sistema')
# else:
#     print('debes iniciar sesion')
#-------------------------------------------------------
# lenguajes = ['python', 'kotlin', 'java', 'javascript']
# for lenguaje in lenguajes:
#     if lenguaje == 'python':
#         print( lenguaje.upper() )
#     else:
#         print(lenguaje)
#-------------------------------------------------------
#-------------------------------------------------------
#---OBJETOS Y DICCIONARIOS---
#creamos un diccionario simple

# cancion = {
#     'artista' : 'Metallica', #clave y valor
#     'cancion' : 'enter sandman',
#     'lanzamiento' : 1992,
#     'likes' : 3000
# }

# #acceder a los elementos del diccionario
# print(cancion['artista'])
# print(cancion['lanzamiento'])

# #mezclar con strings
# artista = cancion['artista']
# print(f'Estoy escuchando a {artista}')

# print(cancion)

# #agregar nuevos valores
# cancion['playlist'] = 'heavy metal'
# print(cancion)

# #Reemplazar valor existente
# cancion['cancion'] = 'seek & destroy'
# print(cancion)

# #eliminar valor
# del cancion['lanzamiento']
# print(cancion)
#-------------------------------------------------------
#iniciar diccionario vacio
# jugador = {}
# print(jugador)

# #se une jugador
# jugador['nombre'] = 'juan'
# jugador['puntaje'] = 0
# print(jugador)

# #incrementar puntaje
# jugador['puntaje'] = 100
# print(jugador)

# #incrementar puntaje
# jugador['puntaje'] = 200
# print(jugador)

# #acceder a un valor
# print(jugador.get('consola', '¡No existe ese valor!'))

# #iterar en el diccionario
# for llave, valor in jugador.items():
#     print(valor)

# #eliminar jugador y puntaje
# del jugador['nombre']
# del jugador['puntaje']
# print(jugador)
#-------------------------------------------------------
#-------------------------------------------------------
# #ENTRADA DE DATOS DEL USUARIO

# nombre = input('cual es tu nombre:\r\n')
# print(f'hola {nombre}')

# print( 9 % 2)

# leer datos que seran numeros
# edad = input('cual es tu edad? \r\n')
# convertir edad (string) a (int)
# edad = int(edad)

# if edad >= 18:
#     print('ya puedes votar')
# else:
#     print('aun no puedes votar')

# mezclarlo con operadores
# numero = input('agrega un numero y te dire si es par o impar: \r\n')
# numero = int(numero)

# if numero % 2 == 0:
#     print(f'el numero {numero} es par')
# else:
#     print(f'el numero {numero} es impar')
#-------------------------------------------------------
#---EJERCICIO---
# PUNTOS = 0

# def evaluar_respuesta(pregunta, respuesta_correcta):
#     respuesta = input(pregunta)
#     if respuesta.lower() == respuesta_correcta:
#         print('correcto')
#         return 1
#     else:
#         print('incorrecto')
#         return 0

# PUNTOS += evaluar_respuesta('¿Es el número 5 par? \r\n', 'no')
# PUNTOS += evaluar_respuesta('¿Es el número 4 par? \r\n', 'si')
# PUNTOS += evaluar_respuesta('¿Es el número 3 par? \r\n', 'no')

# print(f'Conseguiste {PUNTOS} de 3 puntos')

#-------------------------------------------------------
#-------------------------------------------------------
# #---bucles while y for---
# pregunta = 'agrega un numero y te dire si es par o impar \r\n'
# pregunta += '(escribe "cerrar" para salir de la aplicacion) \r\n'
# preguntar = True

# while preguntar: 
#     # mezclarlo con operadores
#     numero = input(pregunta)

#     if numero == 'cerrar':
#          preguntar = False
#     else:
#         numero = int(numero)

#         if numero % 2 == 0:
#             print(f'el numero {numero} es par')
#         else:
#             print(f'el numero {numero} es impar')

#WHILE

# numero = 0
# # while numero <= 10:
# #     print(numero)
# #     numero +=1 #incremento para evitar loop infinito

# #if dentro del while
# while numero <= 10:
#     if numero == 5:
#         break
#     else:
#         print(numero)
#     numero +=1

#-------------------------------------------------------
#-------------------------------------------------------
#PROYECTO PLAYLIST
#app playlist

playlist = {} #diccionario vacio
playlist['canciones'] = [] #lista vacia de canciones

#funcion principal
def app():
   
   #agregar playlist
   agregar_playlist = True
   while agregar_playlist:
       nombre_playlist = input('¿Como deseas nombrar la playlist?\r\n')
       if nombre_playlist:
           playlist['nombre'] = nombre_playlist

           #ya hay nombre, desactivar true
           agregar_playlist = False

           #llamar funcion para agregar canciones
           agregar_canciones()           

def agregar_canciones():
    #bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        #preguntar al usuario que cancion quiere agregar
        nombre_playlist = playlist['nombre']

        pregunta = f'agrega canciones para la playlist {nombre_playlist}:\r\n'
        pregunta += 'Escribe "x" para dejar de agregar canciones\n\r' 

        cancion = input(pregunta)

        if cancion == 'x':
            #deja de agregar canciones
            agregar_cancion = False

            #mostrar resumen playlist
            mostrar_resumen()
        else:
            #agregar las canciones a la playlist
            playlist['canciones'].append(cancion)

            

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'playlist: {nombre_playlist}\r\n')
    print('canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()