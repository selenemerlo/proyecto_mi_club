class Persona:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):

        self.nombre_completo = nombre_completo
        self.edad = edad
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad

    
    def mostrar_datos(self):
        return f'nombre:{self.nombre_completo}, edad de la persona:{self.edad}, tipo de identicacion: {self.get_tipo_identificacion()}, identifacion:{self.get_identificacion()}, nacionalidad{self.get_nacionalidad()}'
    
    def get_tipo_identificacion(self):
        return self.__tipo_identificacion
    def set_tipo_identificacion(self, tipo_identificacion_modificada):
        self.__tipo_identificacion = tipo_identificacion_modificada

    def get_identificacion(self):
        return self.__identificacion
    def set_identifacion(self, identificacion_modificada):
        self.__identificacion = identificacion_modificada

    def get_nacionalidad(self):
        return self.__nacionalidad
    def set_nacionalidad(self, nacionalidad_modificada):
        self.__nacionalidad = nacionalidad_modificada