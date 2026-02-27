import matplotlib.pyplot as plt 


productos = []
ventas = []

# Deseamos pedir 5 productos.
for i in range(1, 6):
    prod = input("Nombre del producto: ")
    productos.append(prod)
    num = int(input("Introduce numero de ventas: "))
    ventas.append(num)

# Asignamos los valores y mostramos el grafico.
plt.pie(ventas, labels=productos)
plt.show()