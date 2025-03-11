import sqlite3
import matplotlib.pyplot as plt

# Conectar a la base de datos SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Obtener datos de la base de datos
cursor.execute("SELECT name, price FROM producto")
filas = cursor.fetchall()

# Separar las categorías y los valores en listas
categorias = [fila[0] for fila in filas]
valores = [fila[1] for fila in filas]

# Crear gráfico de barras
plt.bar(categorias, valores, color='lightgreen')

# Agregar etiquetas y título
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')

# Mostrar gráfico
plt.show()

# Cerrar conexión a la base de datos
conn.close()
