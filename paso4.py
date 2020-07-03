def calculo_prima_emision(n_acciones,v_nominal,desembolso_accionistas):
	"""
	n_acciones,
	v_nominal,
	desembolso_accionistas
	"""
	prima_emision_total = (
		desembolso_accionistas - n_acciones*v_nominal
	)
	prima_emision=prima_emision_total/n_acciones
	'''
	print(v_nominal,'Precio de la acción')
	print(prima_emision_total,'Prima de emisión total')
	print(prima_emision,'Prima de emisión')
	print(v_nominal+prima_emision,'Precio emisión')
	'''
	return v_nominal+prima_emision
	

print(calculo_prima_emision(30000,5,240000))
print(calculo_prima_emision(50000,5,300000))