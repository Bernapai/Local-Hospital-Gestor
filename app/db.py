import sqlite3

try:
    # Mantén la conexión abierta
    db = sqlite3.connect('C:\\Users\\Meunier\\Documents\\ProyectosPersonales\\BasesLocales\\Hospital.db') #Aca iria la ruta de la base de datos suya
    cursor = db.cursor()
except sqlite3.Error as e:
    print(f"Error de base de datos: {e}")  