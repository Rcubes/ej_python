import time
import winsound

minutos = int(input('Ingresa el número de minutos: '))
segundos = int(input('Ingresa el número de segundos: '))
partimos = input('Partimos? [y/n]: ')

valor = 60*minutos + segundos

if partimos == 'y':
    print('Partimos Entonces!!!')
    while valor >= 0:
    
        if valor >= 60 and valor % 60 == 0:
            print(f'\u2022 Te queda(n) {int(valor/60)} minuto(s)')
        elif valor % 10 == 0 and valor != 0:
            print(f'\u2022 Te quedan {valor} segundos')
        elif valor == 0:
            winsound.Beep(1000,1000)
            print(f'\u2022 {valor}!')
        elif valor < 10:
            winsound.Beep(1000,100)
            print(f'\u2022 {valor}!')

        time.sleep(1)
        valor -= 1

    print('Se acabó el Tiempo!!!')

else: 
    print('Bueno, nos vemos la Próxima')