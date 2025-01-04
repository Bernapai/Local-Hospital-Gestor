from models.cita import Cita
from db import db ,cursor


class CitaServices ():
  
    def agregarCita(self, cita:Cita):
        try:
            cursor.execute("INSERT INTO citas (id_paciente, id_medico, fecha, hora) VALUES (?, ?, ?, ?)", (cita.get_paciente_id(), cita.get_medico_id(), cita.get_fecha(), cita.get_fecha()))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False
    
    def obtenerCitas(self):
        try:
            cursor.execute("SELECT * FROM citas")
            citas = cursor.fetchall()
            return citas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

        
    def obtenerCita(self, id_cita):
        try:
            cursor.execute("SELECT * FROM citas WHERE id = ?", (id_cita,))
            cita = cursor.fetchone()
            return cita
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def eliminarCita(self, id_cita):
        try:
            cursor.execute("DELETE FROM citas WHERE id = ?", (id_cita,))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False

    def actualizarCita(self, id_cita, cita:Cita):
        try:
            cursor.execute("UPDATE citas SET id_paciente = ?, id_medico = ?, fecha = ?, hora = ? WHERE id = ?", 
                       (cita.get_paciente_id(), cita.get_medico_id(), cita.get_fecha(), cita.get_hora(), id_cita))
            db.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return False


    def obtenerCitasPorPaciente(self, id_paciente):
        try:
            cursor.execute("SELECT * FROM citas WHERE id_paciente = ?", (id_paciente,))
            citas = cursor.fetchall()
            return citas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerCitasPorMedico(self, id_medico):
        try:
            cursor.execute("SELECT * FROM citas WHERE id_medico = ?", (id_medico,))
            citas = cursor.fetchall()
            return citas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerCitasPorFecha(self, fecha):
        try:
            cursor.execute("SELECT * FROM citas WHERE fecha = ?", (fecha,))
            citas = cursor.fetchall()
            return citas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def obtenerCitasPorHora(self, hora):
        try:
            cursor.execute("SELECT * FROM citas WHERE hora = ?", (hora,))
            citas = cursor.fetchall()
            return citas
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    