import sqlite3



try:
    # Mantén la conexión abierta
    db = sqlite3.connect('Hospital.db')
    cursor = db.cursor()
except sqlite3.Error as e:
    print(f"Error de base de datos: {e}")
