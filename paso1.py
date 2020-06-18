# para el próximo día: encapsulamos código
def desglose(total,tipo_iva):
	bi=round(total/(1+tipo_iva/100),2)
	print(bi)
	print('+',round(bi*tipo_iva/100,2),sep='')
	print('-----')
	print(round(bi*(1+tipo_iva/100),2))


desglose(100,7)

'''
100
+21
---
121
'''


'''
n=3
for i in range(n):
	print(i)
'''


'''
for j in range(1,11):
	print('Tabla del ',j)
	for i in range(1,11):
		if i!=5:
			print(j,' x ',i,' = ',j*i)
'''