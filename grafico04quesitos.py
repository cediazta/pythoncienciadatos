import matplotlib.pyplot as plt 

# La mayoria de los graficos dibujan sus elementos a partir de datos X e Y.
# Clubes (X)
equipos = ["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]
# Valor de mercado (Y)
valores = [30, 400, 66, 20]

# Para crear el grafico debemos darle los datos a la libreria mediante plt.bar
plt.pie(valores ,labels=equipos)

# Personalizamos el grafico.
plt.title("Grafico Quesitos")
plt.xlabel("Presupuestos")

# Podemos guardar los graficos en imagenes.
plt.savefig('images/quesitos.png')
plt.show()



