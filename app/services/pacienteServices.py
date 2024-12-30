from models.paciente import Paciente
from db import db ,cursor
import sqlite3


class PacienteServices ():

    def agregarPaciente(self, paciente:Paciente):
        try:
            cursor.execute("INSERT INTO pacientes (nombre, apellido, dni, direccion, telefono) VALUES (?, ?, ?, ?, ?)", (paciente.nombre, paciente.apellido, paciente.dni, paciente.direccion, paciente.telefono))
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
            return False

    def obtenerPaciente(self, id_paciente):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE id_paciente = ?", (id_paciente,))
            paciente = cursor.fetchone()
            return paciente
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def eliminarPaciente(self, id_paciente):
        try:
            cursor.execute("DELETE FROM pacientes WHERE id_paciente = ?", (id_paciente,))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def actualizarPaciente(self, paciente:Paciente):
        try:
            cursor.execute("UPDATE pacientes SET nombre = ?, apellido = ?, dni = ?, direccion = ?, telefono = ? WHERE id_paciente = ?", (paciente.nombre, paciente.apellido, paciente.dni, paciente.direccion, paciente.telefono, paciente.id_paciente))
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
            