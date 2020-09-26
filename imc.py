peso = int(input('Ingrese su peso en KG:\n>'))
altura = int(input('Ingrese su altura en cm:\n>'))

imc = peso/(altura/100)**2

if imc < 18:
    estado = 'Bajo Peso'
elif imc < 25:
    estado = 'Adecuado'
elif imc < 30:
    estado = 'Sobrepreso'
elif imc < 35:
    estado = 'Obesidad Grado 1'
elif imc < 40:
    estado = 'Obesidad Grado 2'
else:
    estado = 'Obesidad Grado 3'


print(f'Tu IMC es: {imc}')
print(f'Clasificación OMS: {estado}')
