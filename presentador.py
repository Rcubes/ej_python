nombre = input('Ingrese su Nombre: ')
sexo = input('Ingrese Género [F o M]: ')
edad = input('Ingrese Edad: ')
ocupacion = input('Ingrese Ocupación: ')
lugar = input('En dónde?: ')
caracteristica_1 = input('Ingrese 3 características:\n1. > ')
caracteristica_2 = input('2. > ')
caracteristica_3 = input('3. > ')
programar = input('Sabes programar? [y/n]: ')
math = input('Te gustan las matemáticas? [y/n]: ')

if sexo.upper() == 'F':
    parte = 'una mujer'
elif sexo.upper() == 'M':
    parte =  'un hombre'
else:
    parte = 'un ente'
    
if programar.upper() == 'Y':
    resp_p = 'Sí'
else:
    resp_p = 'No'
    
if math.upper() == 'Y':
    resp_m = 'me gustan las matemáticas'
else:
    resp_m = 'no me gustan las matemáticas'
        

print(f'''

Hola soy {nombre}, tengo {edad} años y me desempeño como {ocupacion} en {lugar}.
Me considero {parte} {caracteristica_1}, {caracteristica_2} y {caracteristica_3}.

{resp_p} sé programar y {resp_m}.
''')
