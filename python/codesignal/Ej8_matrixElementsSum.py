# After becoming famous, the CodeBots decided to move into a new building together.
# Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious,
# they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.
# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room,
# your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

matrix = [[0,1,1,2], 
          [0,5,0,0], 
          [2,0,3,3]]
# Expected output: 9

# IDEA: Pasar 2 contadores simultaneamente: 1 para la fila de arriba otro para la de abajo.
# El contador de arriba chequea si hay una posicion con el valor 0, si no hay 0 el valor de esa posicion del contador de abajo lo añade a un diccionario para sumar,
# así hasta que se acabe la fila y pasa a la siguiente.