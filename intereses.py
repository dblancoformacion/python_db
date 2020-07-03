# Calculadora de intereses

def cuota(capital,tipo,meses,pagos_anuales):
	interes=(1+tipo/100)**(1/pagos_anuales)-1 # 12 por ser tipo de interés anual
	interes*=100
	return round(
		capital*interes
		/
		(
			100*(1-(1+interes/100)**(-meses))
		)
		,2)
	

capital=5000
meses=12
tipo=5
pagos_anuales=12

pago=cuota(capital,tipo,meses,pagos_anuales)
print('Cuota: ',pago)
print('Intereses abonados en total: ',round(pago*meses-capital,2))

