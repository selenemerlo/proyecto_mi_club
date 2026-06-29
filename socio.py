from persona import Persona

class Socio(Persona):
    def __init__(self, fecha_inscripcion, estado, usuario, contrasenia, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        super().__init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad)
        self.lista_clubes = []
        self.lista_cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado
        self.__usuario = usuario
        self.__contrasenia = contrasenia


    def get_usuario(self):
        return self.__usuario
    def set_usuario (self, usuario_nuevo):
        self.__usuario = usuario_nuevo


    def get_contrasenia(self):
        return self.__contrasenia
    def set_contrasenia(self, contrasenia_nueva):
        self.__contrasenia = contrasenia_nueva

    