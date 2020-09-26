import math

import os
os.system('cls')


digitos = [2,3,4,5,6,7]
rut_invertido = input('Ingresa tu RUT: ')[::-1]
largo_rut = len(rut_invertido)
reps = math.ceil(largo_rut/ 6)
digitos *= reps

#resultado = []
# for d,n in zip(digitos[:largo_rut],rut_invertido):
#     resultado.append(int(n)*d)

resultado = [int(n)*d for d,n in zip(digitos[:largo_rut],rut_invertido)]

final = sum(resultado) % 11
verificador = 11-final

if verificador == 10:
    verificador = 'k'
elif verificador == 11:
    verificador = 0

print(f'Su dígito verificador es {verificador}')
