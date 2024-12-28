
class Medico ():
    def __init__(self, nombre : str, apellido : str, especialidad : str, telefono : str):
        if not isinstance (nombre, str):
            raise ValueError(f'Error')
        if not isinstance (apellido, str):
            raise ValueError(f'Error')
        if not isinstance (especialidad, str):
            raise ValueError(f'Error')
        if not isinstance (telefono, str):
            raise ValueError(f'Error')
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__especialidad = especialidad
        self.__telefono = telefono

      # Getters
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_especialidad(self):
        return self.__especialidad

    def get_telefono(self):
        return self.__telefono