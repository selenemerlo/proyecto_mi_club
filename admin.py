class Administrador:
    def __init__(self,nombre, usuario, contrasenia):
        self.nombre = nombre
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def get_usuario(self):
        return self.__usuario
    def set_usuario(self, usuario_modificado):
        self.__usuario = usuario_modificado

    def get_contrasenia (self):
        return self.__contrasenia
    def set_contrasenia(self, contrasenia_modificada):
        self.__contrasenia = contrasenia_modificada

