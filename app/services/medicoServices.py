from models.medico import Medico
from db import db ,cursor
import sqlite3


class MedicoServices ():

    def agregarMedico(self, medico:Medico):
        try:
            cursor.execute("INSERT INTO medicos (nombre, apellido, especialidad) VALUES (?, ?, ?)", (medico.get_nombre(), medico.get_apellido(), medico.get_especialidad()))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerMedicos(self):
        try:
            cursor.execute("SELECT * FROM medicos")
            medicos = cursor.fetchall()
            return medicos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerMedico(self, id):
        try:
            cursor.execute("SELECT * FROM medicos WHERE id = ?", (id,))
            medico = cursor.fetchone()
            return medico
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def eliminarMedico(self, id):
        try:
            cursor.execute("DELETE FROM medicos WHERE id = ?", (id,))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def actualizarMedico(self, id_medico, medico:Medico):
        try:
            cursor.execute("UPDATE medicos SET nombre = ?, apellido = ?, especialidad = ? WHERE id = ?", 
                           (medico.get_nombre(), medico.get_apellido(), medico.get_especialidad(), id_medico))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False



    def obtenerMedicosPorEspecialidad(self, especialidad):
        try:
            cursor.execute("SELECT * FROM medicos WHERE especialidad = ?", (especialidad,))
            medicos = cursor.fetchall()
            return medicos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerMedicosPorNombre(self, nombre):
        try:
            cursor.execute("SELECT * FROM medicos WHERE nombre = ?", (nombre,))
            medicos = cursor.fetchall()
            return medicos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerMedicosPorApellido(self, apellido):
        try:
            cursor.execute("SELECT * FROM medicos WHERE apellido = ?", (apellido,))
            medicos = cursor.fetchall()
            return medicos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerMedicosPorNombreYApellido(self, nombre, apellido):
        try:
            cursor.execute("SELECT * FROM medicos WHERE nombre = ? AND apellido = ?", (nombre, apellido))
            medicos = cursor.fetchall()
            return medicos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    