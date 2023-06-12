#Dado un número que representa un tiempo en segundos y que se pedirá al usuario, calcular ese tiempo expresado en horas, minutos y segundos.

numero = int(input('Introduzca tiempo en segundos: \r\n'))

if numero >= 3600:
    
    horas = int(numero / 3600)
    minutos = int(horas % 3600)
    
    print(f'{numero}s son {horas}h, {minutos}m')
elif numero >= 60:
   
    minutos = int(numero / 60)
    segundos = int(numero % 60)
    
    print(f'{numero}s son {minutos}m, {segundos}s')
else:
    print(f'{numero}s son {numero}s')

#horas = segundos × 3600 o minutos × 60
