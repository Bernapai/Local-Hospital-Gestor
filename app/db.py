import sqlite3

db = None
cursor = None

try:
    # Mantén la conexión abierta
    db = sqlite3.connect('Hospital.db')
    cursor = db.cursor()
except sqlite3.Error as e:
    print(f"Error de base de datos: {e}")
finally:
    # Asegúrate de cerrar la conexión a la base de datos si fue abierta
    if db:
        db.close()
