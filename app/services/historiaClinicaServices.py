from models.historia_clinica import HistoriaClinica
from db import db ,cursor
import sqlite3


class HistoriaClinicaServices ():
    def agregarHistoriaClinica(self, historiaClinica:HistoriaClinica):
        try:
            cursor.execute("INSERT INTO historias_clinicas (id_paciente, fecha, diagnostico, tratamiento, id_medico) VALUES (?, ?, ?, ?, ?)", (historiaClinica.get_paciente_id(), historiaClinica.get_fecha(), historiaClinica.get_diagnostico(), historiaClinica.get_tratamiento(), historiaClinica.get_medico_id()))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerHistoriasClinicas(self):
        try:
            cursor.execute("SELECT * FROM historias_clinicas")
            historias_clinicas = cursor.fetchall()
            return historias_clinicas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerHistoriaClinica(self, id_historia_clinica):
        try:
            cursor.execute("SELECT * FROM historias_clinicas WHERE id_historia_clinica = ?", (id_historia_clinica,))
            historia_clinica = cursor.fetchone()
            return historia_clinica
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def eliminarHistoriaClinica(self, id_historia_clinica):
        try:
            cursor.execute("DELETE FROM historias_clinicas WHERE id_historia_clinica = ?", (id_historia_clinica,))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

   def actualizarHistoriaClinica(self, id_historia_clinica, historiaClinica:HistoriaClinica):
        try:
            cursor.execute("UPDATE historias_clinicas SET id_paciente = ?, fecha = ?, diagnostico = ?, tratamiento = ?, id_medico = ? WHERE id_historia_clinica = ?", 
                       (historiaClinica.get_paciente_id(), historiaClinica.get_fecha(), historiaClinica.get_diagnostico(), historiaClinica.get_tratamiento(), historiaClinica.get_medico_id(), id_historia_clinica))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False


    def obtenerHistoriasClinicasPorPaciente(self, id_paciente):
        try:
            cursor.execute("SELECT * FROM historias_clinicas WHERE id_paciente = ?", (id_paciente,))
            historias_clinicas = cursor.fetchall()
            return historias_clinicas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerHistoriasClinicasPorMedico(self, id_medico):
        try:
            cursor.execute("SELECT * FROM historias_clinicas WHERE id_medico = ?", (id_medico,))
            historias_clinicas = cursor.fetchall()
            return historias_clinicas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerHistoriasClinicasPorFecha(self, fecha):
        try:
            cursor.execute("SELECT * FROM historias_clinicas WHERE fecha = ?", (fecha,))
            historias_clinicas = cursor.fetchall()
            return historias_clinicas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerHistoriasClinicasPorDiagnostico(self, diagnostico):
        try:
            cursor.execute("SELECT * FROM historias_clinicas WHERE diagnostico = ?", (diagnostico,))
            historias_clinicas = cursor.fetchall()
            return historias_clinicas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def obtenerHistoriasClinicasPorTratamiento(self, tratamiento):
        try:
            cursor.execute("SELECT * FROM historias_clinicas WHERE tratamiento = ?", (tratamiento,))
            historias_clinicas = cursor.fetchall()
            return historias_clinicas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False