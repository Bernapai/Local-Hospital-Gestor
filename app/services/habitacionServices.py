from models.habitacion import Habitacion
from db import db ,cursor
import sqlite3

class HabitacionServices ():

    def agregarHabitacion(self, habitacion:Habitacion):
        try:
            cursor.execute("INSERT INTO habitaciones (numero, tipo,capacidad, estado) VALUES (?, ?, ?, ?)", (habitacion.get_numero(), habitacion.get_tipo(), habitacion.get_capacidad(), habitacion.get_estado()))
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
            return []
    
    def obtenerHabitacion(self, id):
        try:
            cursor.execute("SELECT * FROM habitaciones WHERE id = ?", (id,))
            habitacion = cursor.fetchone()
            return habitacion
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []
    
    def eliminarHabitacion (self, id):
        try:
            cursor.execute("DELETE FROM habitaciones WHERE id = ?", (id,))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False


    def actualizarHabitacion(self, id_habitacion, habitacion:Habitacion):
        try:
            cursor.execute("UPDATE habitaciones SET numero = ?, tipo = ?, capacidad = ?, estado = ? WHERE id = ?", 
                       (habitacion.get_numero(), habitacion.get_tipo(), habitacion.get_capacidad(), habitacion.etado(), id_habitacion))
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
            return []


    def obtenerHabitacionesPorPrecio(self, precio):
        try:
            cursor.execute("SELECT * FROM habitaciones WHERE precio = ?", (precio,))
            habitaciones = cursor.fetchall()
            return habitaciones
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerHabitacionesPorNumero(self, numero):
        try:
            cursor.execute("SELECT * FROM habitaciones WHERE numero = ?", (numero,))
            habitaciones = cursor.fetchall()
            return habitaciones
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerHabitacionesPorTipoYPrecio(self, tipo, precio):
        try:
            cursor.execute("SELECT * FROM habitaciones WHERE tipo = ? AND precio = ?", (tipo, precio))
            habitaciones = cursor.fetchall()
            return habitaciones
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

            



    

 