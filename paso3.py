# Cálculo de reservas
beneficio = 6000

reservas={
	'estatutaria' : 0.25,
	'legal' : 0.1,
	'voluntaria' : .06,
	}

print(reservas['legal'])

total_reservas=0
for i in reservas:
	print(round(reservas[i]*beneficio,2),i)
	total_reservas+=reservas[i]

dividendo = beneficio*(1-total_reservas)
print('-----')
print(round(dividendo,2))