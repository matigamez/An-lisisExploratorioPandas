import pandas as pd

# Carga el archivo retail_sales.csv en un DataFrame de Pandas
df = pd.read_csv('./data/retail_sales_dataset.csv')

# Muestra las primeras 10 filas del DataFrame
print("Primeras 10 filas del DataFrame:")
print(df.head(10))

# Exploración Inicial de los Datos
print("\nÚltimas 5 filas del DataFrame:")
print(df.tail())

print("\nInformación general del DataFrame:")
print(df.info())

print("\nEstadísticas descriptivas del DataFrame:")
print(df.describe())

# Inspección de los Datos
print("\nTipos de datos de cada columna:")
print(df.dtypes)

print("\nConteo de valores únicos en la columna 'Product Category':")
print(df['Product Category'].value_counts())
#No existe columna Tienda
#print("\nValores únicos en la columna 'Tienda':")
#print(df['Tienda'].unique())  

# Filtrado de Datos
print("\nFilas donde Ventas > 50:")
print(df[df['Total Amount'] > 50])

print("\nFilas donde Precio < 0.5:")
print(df[df['Price per Unit'] < 0.5])

print("\nFilas donde Product Category es 'Manzanas' y Ventas > 30:")
print(df.query("`Product Category` == 'Manzanas' and `Total Amount` > 30"))

# Slicing de Datos
print("\nSeleccionando columnas 'Product Category' y 'Total Amount':")
print(df[['Product Category', 'Total Amount']])

#print("\nFilas de la 5 a la 10 (inclusive) y columnas 'Product Category' y 'Tienda':")
#print(df.loc[4:9, ['Product Category', 'Tienda']])  # Ajusta la selección según la estructura de tus datos

print("\nPrimeras 5 filas y primeras 3 columnas del DataFrame:")
print(df.iloc[:5, :3])  # iloc excluye el límite superior
