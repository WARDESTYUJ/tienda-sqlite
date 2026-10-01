import sqlite3
conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")
print("✅ Conexión a tienda.db exitosa")
cursor.close()
conn.close()