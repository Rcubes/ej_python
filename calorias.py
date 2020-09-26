import sys 

carbo = float(sys.argv[1])
grasa = float(sys.argv[2])
prote = float(sys.argv[3])

calorias = 4 * (carbo + prote) + 9 * grasa

print(f'La cantidad de calorías es: {calorias}')