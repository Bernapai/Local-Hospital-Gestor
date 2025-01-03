from models.paciente import Paciente
from db import db ,cursor
import sqlite3


class PacienteServices ():

    def agregarPaciente(self, paciente:Paciente):
        try:
            cursor.execute("INSERT INTO pacientes (nombre, apellido, edad, direccion, enfermedad) VALUES (?, ?, ?, ?, ?)", (paciente.get_nombre(), paciente.get_apellido(), paciente.get_edad(), paciente.get_direccion(), paciente.get_enfermedad()))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerPacientes(self):
        try:
            cursor.execute("SELECT * FROM pacientes")
            pacientes = cursor.fetchall()
            return pacientes
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerPaciente(self, id_paciente):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE id_paciente = ?", (id_paciente,))
            paciente = cursor.fetchone()
            return paciente
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def eliminarPaciente(self, id_paciente):
        try:
            cursor.execute("DELETE FROM pacientes WHERE id_paciente = ?", (id_paciente,))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def actualizarPaciente(self, id_paciente, paciente:Paciente):
        try:
            cursor.execute("UPDATE pacientes SET nombre = ?, apellido = ?, dni = ?, direccion = ?, telefono = ? WHERE id_paciente = ?", 
                           (paciente.get_nombre(), paciente.get_apellido(), paciente.get_dni(), paciente.get_direccion(), paciente.get_telefono(), id_paciente))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False


    def obtenerPacientesPorDni(self, dni):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE dni = ?", (dni,))
            pacientes = cursor.fetchall()
            return pacientes
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False


    def obtenerPacientesPorNombre(self, nombre):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE nombre = ?", (nombre,))
            pacientes = cursor.fetchall()
            return pacientes
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerPacientesPorApellido(self, apellido):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE apellido = ?", (apellido,))
            pacientes = cursor.fetchall()
            return pacientes
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerPacientesPorTelefono(self, telefono):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE telefono = ?", (telefono,))
            pacientes = cursor.fetchall()
            return pacientes
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerPacientesPorDireccion(self, direccion):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE direccion = ?", (direccion,))
            pacientes = cursor.fetchall()
            return pacientes
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False


    def obtenerPacientesPorNombreYApellido(self, nombre, apellido):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE nombre = ? AND apellido = ?", (nombre, apellido))
            pacientes = cursor.fetchall()
            return pacientes
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False
            