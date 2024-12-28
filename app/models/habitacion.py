
class Habitacion ():
    def __init__(self, numero:int, tipo :str, capacidad:str , estado:str):
        if not isinstance (numero, int) or numero < 0:
            raise ValueError(f'Error')
        if not isinstance (tipo, str):
            raise ValueError(f'Error')
        if not isinstance (capacidad, str):
            raise ValueError(f'Error')
        if not isinstance (estado, str):
            raise ValueError(f'Error')
        
        self.__numero = numero
        self.__tipo = tipo
        self.__capacidad = capacidad
        self.__estado = estado

     # Getters
    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def get_capacidad(self):
        return self.__capacidad

    def get_estado(self):
        return self.__estado
