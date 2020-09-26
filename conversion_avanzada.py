clp_sol = 0.0046
clp_parg = 0.093
clp_usd = 0.00013
clp_clp = 1

sol_clp = 219.07
sol_parg = 20.33
sol_usd = 0.28
sol_sol = 1

parg_clp = 10.78
parg_sol = 0.049
parg_usd = 0.014
parg_parg = 1

usd_clp = 774.30
usd_sol = 3.53
usd_parg = 71.84
usd_usd = 1

print('Qué moneda desea cambiar?')
print('SOL: Sol Peruano')
print('PARG: Peso Argentino')
print('USD: Dólar Americano')
print('CLP: Peso Chileno')

moneda_desde = input('> ').upper()

if moneda_desde == 'SOL':
    var_d = 'Soles Peruanos'
elif moneda_desde == 'PARG':
    var_d = 'Pesos Argentinos'
elif moneda_desde == 'USD':
    var_d = 'Dólares'
else:
    var_d = 'Pesos Chilenos'

monto_desde = int(input(f'Ingrese Monto en {var_d}: '))

print('A qué moneda desea cambiar?')
print('SOL: Sol Peruano')
print('PARG: Peso Argentino')
print('USD: Dólar Americano')
print('CLP: Peso Chileno')

moneda_a = input('> ').upper()

if moneda_a == 'SOL':
    var_a = 'Soles Peruanos'
elif moneda_a == 'PARG':
    var_a = 'Pesos Argentinos'
elif moneda_a == 'USD':
    var_a = 'Dólares'
else:
    var_a = 'Pesos Chilenos'

if moneda_desde == 'SOL':
    if moneda_a == 'SOL':
        monto_a = sol_sol*monto_desde
    elif moneda_a == 'PARG':
        monto_a = sol_parg*monto_desde
    elif moneda_a == 'USD':
        monto_a = sol_usd*monto_desde
    else:
        monto_a = sol_clp*monto_desde
    
elif moneda_desde == 'PARG':
    if moneda_a == 'SOL':
        monto_a = parg_sol*monto_desde
    elif moneda_a == 'PARG':
        monto_a = parg_parg*monto_desde
    elif moneda_a == 'USD':
        monto_a = parg_usd*monto_desde
    else:
        monto_a = parg_clp*monto_desde
        
elif moneda_desde == 'USD':
    if moneda_a == 'SOL':
        monto_a = usd_sol*monto_desde
    elif moneda_a == 'PARG':
        monto_a = usd_parg*monto_desde
    elif moneda_a == 'USD':
        monto_a = usd_usd*monto_desde
    else:
        monto_a = usd_clp*monto_desde
else:
    if moneda_a == 'SOL':
        monto_a = clp_sol*monto_desde
    elif moneda_a == 'PARG':
        monto_a = clp_parg*monto_desde
    elif moneda_a == 'USD':
        monto_a = clp_usd*monto_desde
    else:
        monto_a = clp_clp*monto_desde
    
print(f'Sus {monto_desde} {var_d} corresponden a {monto_a} {var_a}.')
