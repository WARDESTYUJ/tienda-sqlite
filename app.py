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

# ===== ETAPA 4: TABLA VENTAS (llaves foráneas) =====
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        producto_id INTEGER NOT NULL,
        cliente_id INTEGER NOT NULL,
        FOREIGN KEY (producto_id) REFERENCES productos (id),
        FOREIGN KEY (cliente_id) REFERENCES clientes (id)
    )
""")
# ===== ETAPA 5: INSERTAR DATOS (solo si está vacío) =====
cursor.execute("SELECT COUNT(*) FROM productos")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Laptop HP', 1500.00)")
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Mouse Inalámbrico', 25.50)")
    cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES ('Carlos Rojas', '777-12345')")
    cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES ('Maria Lopez', '666-98765')")
    cursor.execute("INSERT INTO ventas (fecha, producto_id, cliente_id) VALUES ('2026-09-29', 1, 1)")
    cursor.execute("INSERT INTO ventas (fecha, producto_id, cliente_id) VALUES ('2026-09-29', 2, 1)")
conn.commit()  # imprescindible en INSERT/UPDATE/DELETE

# ===== CIERRE =====
cursor.close()
conn.close()