from models.habitacion import Habitacion
from db import db ,cursor


class HabitacionServices ():

    def agregarHabitacion(self, habitacion:Habitacion):
        try:
            cursor.execute("INSERT INTO habitaciones (numero, tipo, precio) VALUES (?, ?, ?)", (habitacion.numero, habitacion.tipo, habitacion.precio))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerHabitaciones(self):
        try:
            cursor.execute("SELECT * FROM habitaciones")
            habitaciones = cursor.fetchall()
            return habitaciones
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False
    
    def obtenerHabitacion(self, id_habitacion):
        try:
            cursor.execute("SELECT * FROM habitaciones WHERE id_habitacion = ?", (id_habitacion,))
            habitacion = cursor.fetchone()
            return habitacion
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False
    
    def eliminarHabitacion (self, id_habitacion):
        try:
            cursor.execute("DELETE FROM habitaciones WHERE id_habitacion = ?", (id_habitacion,))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False


    def actualizarHabitacion(self, habitacion:Habitacion):
        try:
            cursor.execute("UPDATE habitaciones SET numero = ?, tipo = ?, precio = ? WHERE id_habitacion = ?", (habitacion.numero, habitacion.tipo, habitacion.precio, habitacion.id_habitacion))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    
    def obtenerHabitacionesPorTipo(self, tipo):
        try:
            cursor.execute("SELECT * FROM habitaciones WHERE tipo = ?", (tipo,))
            habitaciones = cursor.fetchall()
            return habitaciones
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False


    def obtenerHabitacionesPorPrecio(self, precio):
        try:
            cursor.execute("SELECT * FROM habitaciones WHERE precio = ?", (precio,))
            habitaciones = cursor.fetchall()
            return habitaciones
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerHabitacionesPorNumero(self, numero):
        try:
            cursor.execute("SELECT * FROM habitaciones WHERE numero = ?", (numero,))
            habitaciones = cursor.fetchall()
            return habitaciones
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerHabitacionesPorTipoYPrecio(self, tipo, precio):
        try:
            cursor.execute("SELECT * FROM habitaciones WHERE tipo = ? AND precio = ?", (tipo, precio))
            habitaciones = cursor.fetchall()
            return habitaciones
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

            



    

 