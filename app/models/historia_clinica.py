from datetime import datetime

class HistoriaClinica:
    def __init__(self, paciente_id: int, fecha: str, diagnostico: str, tratamiento: str, medico_id: int):
        if not isinstance(paciente_id, int) or paciente_id < 0:
            raise ValueError('El ID del paciente debe ser un entero positivo.')
        if not isinstance(medico_id, int) or medico_id < 0:
            raise ValueError('El ID del médico debe ser un entero positivo.')
        if not isinstance(diagnostico, str):
            raise ValueError('El diagnóstico debe ser una cadena de texto.')
        if not isinstance(tratamiento, str):
            raise ValueError('El tratamiento debe ser una cadena de texto.')

        try:
            self.__fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError('La fecha debe estar en el formato YYYY-MM-DD.')
        
        self.__paciente_id = paciente_id
        self.__medico_id = medico_id
        self.__diagnostico = diagnostico
        self.__tratamiento = tratamiento

    # Getters
    def get_paciente_id(self):
        return self.__paciente_id

    def get_fecha(self):
        return self.__fecha

    def get_diagnostico(self):
        return self.__diagnostico

    def get_tratamiento(self):
        return self.__tratamiento

    def get_medico_id(self):
        return self.__medico_id





