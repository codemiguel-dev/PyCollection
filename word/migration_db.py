import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("word/store.db")
cursor = conn.cursor()

# Crear tabla invoice si no existe (para evitar problemas con la clave foránea)
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    date TEXT NOT NULL
)
"""
)

# Crear tabla invoice_item si no existe
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS invoice_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER,
    description TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    total REAL NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoice(id)
)
"""
)

# Crear tabla inventory si no existe
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
"""
)

# Insertar datos en la tabla inventory
cursor.executemany(
    "INSERT INTO inventory (product_name, quantity, price) VALUES (?, ?, ?)",
    [
        ("Laptop", 10, 800.00),
        ("Mouse", 50, 20.00),
        ("Teclado", 30, 35.00),
    ],
)

# Insertar datos en la tabla invoice
cursor.executemany(
    "INSERT INTO invoice (customer_name, date) VALUES (?, ?)",
    [
        ("Juan Pérez", "2025-03-11"),
        ("María González", "2025-03-10"),
    ],
)

# Obtener los IDs de las facturas insertadas
cursor.execute("SELECT id FROM invoice")
invoice_ids = [row[0] for row in cursor.fetchall()]

# Insertar datos en la tabla invoice_item
cursor.executemany(
    "INSERT INTO invoice_item (invoice_id, description, quantity, price, total) VALUES (?, ?, ?, ?, ?)",
    [
        (invoice_ids[0], "Laptop", 1, 800.00, 800.00),
        (invoice_ids[0], "Mouse", 2, 20.00, 40.00),
        (invoice_ids[1], "Teclado", 1, 35.00, 35.00),
    ],
)

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos, tablas y datos insertados correctamente.")
