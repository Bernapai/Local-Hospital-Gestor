import sqlite3

# Usar un bloque try-except-finally para manejar la conexión y asegurarse de que se cierre correctamente
try:
    # Establecer la conexión con la base de datos
    db = sqlite3.connect('Hospital.db')
    cursor = db.cursor()

    # Puedes realizar las operaciones aquí, como consultas o inserciones.
    # cursor.execute("...")

except sqlite3.Error as e:
    # Capturar errores relacionados con SQLite y mostrar el mensaje de error
    print(f"Error de base de datos: {e}")


    # Cerrar el cursor y la conexión después de usarla
    if cursor:
        cursor.close()
    if db:
        db.close()
