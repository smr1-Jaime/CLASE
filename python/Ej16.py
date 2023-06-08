#Teniendo en cuenta que la clave es “eureka”, escribir un algoritmo que nos pida una clave.
#Solo tenemos 3 intentos para acertar, si fallamos los 3 intentos nos mostrará un mensaje indicándonos que hemos agotado esos 3 intentos.
#Si acertamos la clave, saldremos directamente del programa.


correcto = 'eureka'
cont=1

contraseña=input('ingrese la contraseña \r\n')

while correcto != contraseña and cont<=2:
          contraseña=input('ingrese la contraseña \r\n') 
          cont=cont+1
if cont<=2:
          print('acceso permitido')
else:
          print('acceso denegado')

