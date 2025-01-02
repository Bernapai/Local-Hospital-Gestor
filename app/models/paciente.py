
class Paciente:
    def __init__(self, nombre : str, apellido : str, edad : int, direccion : str, enfermedad : str):
        if not isinstance (nombre, str):
            raise ValueError(f'Error')
        if not isinstance (edad, int) or edad < 0:
            raise ValueError(f'Error')
        if not isinstance (direccion, str):
            raise ValueError(f'Error')
        if not isinstance (enfermedad, str):
            raise ValueError(f'Error')

        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__direccion = direccion
        self.__enfermedad = enfermedad

    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_edad(self):
        return self.__edad
    
    def get_direccion(self):
        return self.__direccion

    def get_enfermedad(self):
        return self.__enfermedad

    

