import matplotlib.pyplot as plt


semana = ("lunes", "Martes", "Miercoles", "Jueves", "Viernes")
temperaturas = []

for dia in semana:
    temp = int(input(f"Temperatura de {dia}: "))
    temperaturas.append(temp)

# La ventaja de los grafcos esta en que si introducimos mas series, podemos represntarlas siempre que pongamos labels distintas.
plt.plot(semana, temperaturas, label="Semana 1")
temperaturas2 = [4, 18, 5, 23, 12]
plt.plot(semana, temperaturas2, label="Semana 2")
plt.legend()
plt.title("Temperaturas Febrero")
plt.xlabel("Dia Semana")
plt.ylabel("Temperatura")
plt.show()

