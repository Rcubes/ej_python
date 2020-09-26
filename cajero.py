import time
import sys

def depositar(saldo, cantidad):
    return saldo + cantidad

def girar(saldo, cantidad):
    if cantidad > saldo:
        return False
    else:
        return saldo - cantidad


def mostrar_saldo(saldo = 0):
    
    opcion = ''
    
    while opcion != 4:
        opcion = int(input('''Bienvenido al Banco!!! Escoga una Opción
        1. Consultar Saldo
        2. Hacer Depósito
        3. Realizar Giro
        4. Salir\n> '''))
        
        if opcion < 1 or opcion > 4:
            print('\nElija una opción válida\n\n')
            time.sleep(1)
        else:
            if opcion == 1:
                print(f'\n Su saldo es: {saldo}\n\n')
                time.sleep(1)
            
            elif opcion == 2:
                cantidad = int(input('Cuánto desea depositar? \n> '))
                saldo = depositar(saldo,cantidad)
                print(f'\nSu nuevo Saldo es: ${saldo}\n\n')
                time.sleep(1)
            
            elif opcion == 3:
                if saldo > 0:
                    respuesta = False
                    while respuesta is False:
                        cantidad = int(input('Cuánto desea retirar? \n> '))
                        respuesta = girar(saldo,cantidad)

                        if respuesta is False:
                            print(f"No se puede girar esta cantidad. Su saldo es de ${saldo}\n\n")
                        else:
                            saldo = respuesta
                            respuesta = True
                            print(f'Su nuevo saldo es de: ${saldo}\n\n')
                            time.sleep(1)
                else:
                    print("No puede realizar giros. Su saldo es de $0.\n\n")
                    time.sleep(1)
            else:
                print('Muchas gracias por su visita.')
                

if len(sys.argv) == 2:
    saldo = int(sys.argv[1])
    mostrar_saldo(saldo)
else:
    mostrar_saldo()