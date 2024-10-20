Este trabajo fue realizado en el marco del Curso de analisis de datos con Python en codingdojolatam.la
Instrucciones

Preparación del Entorno
Asegúrate de tener instalado Pandas en tu entorno de trabajo.
Utiliza el archivo retail_sales.csv del proyecto inicial. Si aún no lo tienes, descarga el archivo correspondiente.
Cargar los Datos
Carga el archivo retail_sales.csv en un DataFrame de Pandas.
Muestra las primeras 10 filas del DataFrame para confirmar que los datos se han cargado correctamente.
Exploración Inicial de los Datos
Muestra las últimas 5 filas del DataFrame.
Utiliza el método info() para obtener información general sobre el DataFrame, incluyendo el número de entradas, nombres de las columnas, tipos de datos y memoria utilizada.
Genera estadísticas descriptivas del DataFrame utilizando el método describe().
Inspección de los Datos
Inspecciona los tipos de datos de cada columna utilizando el atributo dtypes.
Cuenta los valores únicos en la columna Producto utilizando el método value_counts().
Muestra todos los valores únicos en la columna Tienda utilizando el método unique().
Filtrado de Datos
Filtra el DataFrame para mostrar solo las filas donde las ventas (Ventas) sean mayores a 50.
Filtra el DataFrame para mostrar solo las filas donde el precio (Precio) sea menor a 0.5.
Utilizando el método query(), filtra el DataFrame para mostrar las filas donde el producto sea Manzanas y las ventas sean mayores a 30.
Slicing de Datos
Selecciona y muestra solo las columnas Producto y Ventas del DataFrame.
Utilizando loc[], selecciona y muestra las filas de la 5 a la 10 (inclusive) y las columnas Producto y Tienda.
Utilizando iloc[], selecciona y muestra las primeras 5 filas y las primeras 3 columnas del DataFrame.
