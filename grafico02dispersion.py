import matplotlib.pyplot as plt 

# La mayoria de los graficos dibujan sus elementos a partir de datos X e Y.
# Clubes (X)
x = ["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]
# Valor de mercado (Y)
y = [30, 400, 66, 20]

# Para crear el grafico debemos darle los datos a la libreria mediante plt.bar
plt.scatter(x, y)

# Personalizamos el grafico.
plt.title("Grafico de Dispersion")
plt.xlabel("Equipos")
plt.ylabel("Presupuesto")

# Podemos guardar los graficos en imagenes.
plt.savefig('images/dispersion.png')
plt.show()



