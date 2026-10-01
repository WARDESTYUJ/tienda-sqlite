import sqlite3

# ===== ETAPA 1: CONEXIÓN =====
conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")
print("✅ Conexión a tienda.db exitosa")

# ===== ETAPA 2: TABLA PRODUCTOS =====
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
""")

# ===== ETAPA 3: TABLA CLIENTES =====
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
""")
# ===== CIERRE =====
cursor.close()
conn.close()