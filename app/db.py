import sqlite3

try:
    # Mantén la conexión abierta
    db = sqlite3.connect('C:\\Users\\Meunier\\Documents\\ProyectosPersonales\\BasesLocales\\Hospital.db')
    cursor = db.cursor()
except sqlite3.Error as e:
    print(f"Error de base de datos: {e}")  