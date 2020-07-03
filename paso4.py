# prima de emisión

n_acciones = 30000 #acciones
v_nominal = 5 # valor nominal por acción
desembolso_accionistas = 240000

# prima de emisión total

prima_emision_total = (
	desembolso_accionistas - n_acciones*v_nominal
)
prima_emision=prima_emision_total/n_acciones

print(v_nominal,'Precio de la acción')
print(prima_emision_total,'Prima de emisión total')
print(prima_emision,'Prima de emisión')
print(v_nominal+prima_emision,'Precio emisión')

