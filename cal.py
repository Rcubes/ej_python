import os
import time
import math

def suma(x,y):
    return float(x + y)

def resta(x,y):
    return float(x - y)

def mult(x,y):
    return float(x*y)

def div(x,y):
    return float(x/y)

def root(x,y):
    return float(math.sqrt(x))

def factorial(x,y):
    cont = 1
    x = int(x)
    for x in  range(1,x+1):
         cont*= x
        
    return float(cont)
    
def val(ans, resultado):
    if ans == 'y':
        x = resultado
        print(f'El resultado anterior es: {resultado}')
    else:
        x = int(input('Ingrese el 1er Número: '))
        
    return x

def output(f,x,y):
    resultado = f(x,y)
    print(resultado)
    
    return resultado

def bienvenida(raiz_act):
    if raiz_act == 'n':
        texto = '''Ingrese Operación
        1. Suma dos Números
        2. Resta dos Números
        3. Multiplica dos Números
        4. Divide dos Números
        9. Configuración
        0. Salir \n>  '''
    else:
        texto = '''Ingrese Operación
        1. Suma dos Números
        2. Resta dos Números
        3. Multiplica dos Números
        4. Divide dos Números
        5. Raíz (NUEVO)*
        6. Factorial (NUEVO)*
        9. Configuración
        0. Salir \n>  '''
    
    return texto

def calculadora():
    ans = ''
    opcion = 10
    resultado = 0
    raiz_act = 'n'
    
    while opcion != 0:
        texto = bienvenida(raiz_act)
        y = 0 # se utiliza para evitar error de validación en división
        os.system('cls')
        print(f'El Resultado es: {resultado}')
        opcion = int(input(texto))
        
        if opcion == 1:
            
            os.system('cls')
            print('Operación de SUMA')
            x = val(ans, resultado)
            y = int(input('Ingrese el 2do Número: '))
            ans = input('Desea guardar el resultado [y/n]: ').lower()
            
            resultado = output(suma,x,y)
            time.sleep(1)
            
            
        elif opcion == 2:
            os.system('cls')
            print('Operación de RESTA')
            x = val(ans, resultado)
            y = int(input('Ingrese el 2do Número: '))
            ans = input('Desea guardar el resultado [y/n]: ')
            
            resultado = output(resta,x,y)
            time.sleep(1)
            
        elif opcion == 3:
            os.system('cls')
            print('Operación de MULTIPLICACIÓN')
            x = val(ans, resultado)
            y = int(input('Ingrese el 2do Número: '))
            ans = input('Desea guardar el resultado [y/n]: ')
            
            resultado = output(mult,x,y)
            time.sleep(1)
            
        elif opcion == 4:
            
            os.system('cls')
            print('Operación de DIVISIÓN')
            x = val(ans, resultado)
            while y == 0: # VALIDACIÓN DE NÚMERO DISTINTO DE CERO
                y = int(input('Ingrese el 2do Número: '))
                if y == 0:
                    print('El 2do Número debe ser distinto de 0')
                
            ans = input('Desea guardar el resultado [y/n]: ')
            
            resultado = output(div,x,y)
            time.sleep(1)
        
        elif opcion == 5 and raiz_act == 'y':
            os.system('cls')
            print('Operación de RAÍZ')
            x = val(ans, resultado)
            ans = input('Desea guardar el resultado [y/n]: ')
            resultado = output(root,x,y)
            time.sleep(1)
            
        elif opcion == 6 and raiz_act == 'y':
            os.system('cls')
            print('Operación de FACTORIAL')
            x = val(ans, resultado)
            ans = input('Desea guardar el resultado [y/n]: ')
            resultado = output(factorial,x,y)
            time.sleep(1)
            
        elif opcion == 9:
            os.system('cls')
            print('CONFIGURACIÓN:')
            raiz_act = input('Desea activar las funciones avanzadas? [y/n]: ').lower()
        else:
            if opcion != 0:
                print('Ingrese una Opción Válida')
                time.sleep(1)
            else:
                os.system('cls')
                print('Muchas gracias por usar esta calculadora')
                time.sleep(2)
                os.system('cls')





calculadora()        