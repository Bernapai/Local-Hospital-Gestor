from datetime import datetime


class Cita ():
    def __init__(self, paciente_id:int ,medico_id:int, fecha:str, hora:str):
        if not isinstance (paciente_id, int) or paciente_id < 0:
            raise ValueError(f'Error')
        if not isinstance (medico_id, int) or medico_id < 0:
            raise ValueError(f'Error')
        if not isinstance (hora, str):
            raise ValueError(f'Error')
        #Validaciaon del formato fecha (por ejemplo, "YYYY-MM-DD")
        try:
            self.__fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError('La fecha debe estar en el formato YYYY-MM-DD')

        # Validación del formato de hora (por ejemplo, "HH:MM")
        try:
            self.__hora = datetime.strptime(hora, "%H:%M").time()
        except ValueError:
            raise ValueError('La hora debe estar en el formato HH:MM.')

    
        self.__paciente_id = paciente_id
        self.__medico_id = medico_id
      



      # Métodos getter para acceder a los atributos privados si es necesario
    def get_paciente_id(self):
        return self.__paciente_id
    
    def get_medico_id(self):
        return self.__medico_id

    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora