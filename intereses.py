# Calculadora de intereses

def cuota(capital,tipo,meses):
	interes=(1+tipo/100)**(1/12)-1 # 12 por ser tipo de interés anual
	interes*=100
	return round(
		capital*interes
		/
		(
			100*(1-(1+interes/100)**(-meses))
		)
		,2)
	

capital=1000
meses=12
tipo=10

pago=cuota(capital,tipo,meses);
print('Cuota mensual : ',pago)
print('Intereses abonados en total: ',round(pago*meses-capital,2))