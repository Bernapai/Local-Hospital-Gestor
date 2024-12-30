from models.medico import Medico
from db import db ,cursor


class MedicoServices ():

    def agregarMedico(self, medico:Medico):
        try:
            cursor.execute("INSERT INTO medicos (nombre, apellido, especialidad) VALUES (?, ?, ?)", (medico.nombre, medico.apellido, medico.especialidad))
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
            return False

    def obtenerMedico(self, id_medico):
        try:
            cursor.execute("SELECT * FROM medicos WHERE id_medico = ?", (id_medico,))
            medico = cursor.fetchone()
            return medico
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def eliminarMedico(self, id_medico):
        try:
            cursor.execute("DELETE FROM medicos WHERE id_medico = ?", (id_medico,))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def actualizarMedico(self, medico:Medico):
        try:
            cursor.execute("UPDATE medicos SET nombre = ?, apellido = ?, especialidad = ? WHERE id_medico = ?", (medico.nombre, medico.apellido, medico.especialidad, medico.id_medico))
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
            return False

    def obtenerMedicosPorNombre(self, nombre):
        try:
            cursor.execute("SELECT * FROM medicos WHERE nombre = ?", (nombre,))
            medicos = cursor.fetchall()
            return medicos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerMedicosPorApellido(self, apellido):
        try:
            cursor.execute("SELECT * FROM medicos WHERE apellido = ?", (apellido,))
            medicos = cursor.fetchall()
            return medicos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerMedicosPorNombreYApellido(self, nombre, apellido):
        try:
            cursor.execute("SELECT * FROM medicos WHERE nombre = ? AND apellido = ?", (nombre, apellido))
            medicos = cursor.fetchall()
            return medicos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    