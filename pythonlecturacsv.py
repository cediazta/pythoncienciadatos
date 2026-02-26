import pandas as pd

# vamos a leer datos de nuestro CSV.
# Creamos un DataFrame a partir del fichero.
df = pd.read_csv('data/datos.csv', delimiter=';')
print(df)

# Podemos indicar el numero de filas a mostrar.
print("---------- Primeras 10 filas ----------")
print(df.head(10))

# Podemos convertir los datos en diccionarios para trabajar con python puro.
diccionario = df.to_dict(orient='records')
for registro in diccionario:
    print(registro)

# Podemos hacer calculos, por ejemplo, la media.
df_media = df['edad'].mean()
print(df_media)

# Podemos agrupar por una columna si lo deseamos.
df_grupo = df.groupby('ocupacion')
print(df_grupo.size())


