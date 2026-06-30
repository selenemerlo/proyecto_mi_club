from clubCategoria import  ClubCategoria
#Importe una clase
class Administrador(ClubCategoria):
    def __init__(self,nombre, descripcion, ubicacion, presidente, fecha_fundacion, usuario, contrasenia):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
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

#nuevos metodos  30/6/26
    def nuevos_socios(self,socios_nuevos):
        self.__socios.append(socios_nuevos)


    def se_portaron_mal(self):
        if self.__socios == "Deuda pendiente" or "Norma/s incumplidas ":
            print("El socio esta suspendido hasta nuevo aviso")


    def verificar_credenciales(self,credencial):
        if credencial != credencial:
            print("La credencial es incorrecta")