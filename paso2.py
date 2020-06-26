def desglose(bi,tipo_iva):
	print(bi,'BI')
	iva=bi*tipo_iva/100
	print(iva,'I.V.A.')
	total=bi+iva
	print(total,'Total Factura')

def desglose2(bi,tipo_iva):
	print(bi)
	print(bi*tipo_iva/100)
	print(bi*(1+tipo_iva/100))

for i in range(100,501,100):
	if i!=300:
		print('-----')
		desglose(i,21)

