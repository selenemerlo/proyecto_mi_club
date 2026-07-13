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

    
#1-Permitir que un socio pueda asociarse a uno o más clubes.
    




#2-Permitir que un socio deje de pertenecer a un club determinado.
    def eliminar_de_club(self, usuario):
        self.lista_clubes.remove(usuario)




#4-Registrar el pago de una cuota pendiente.

    def





#Cambiar el estado de un socio activo a suspendido cuando corresponda.
    def estado_socio(self):
        if self.estado == "activo":
                self.estado = "suspendido"
                print("El usuario ha sido suspendido")
        else:
            print("El usuario sigue activo")



#Reactivar un socio suspendido para que pueda volver a utilizar los servicios del club.

    def reactivar_socio(self):
        if self.estado == "suspendido":
            self.estado = "activo"
            print("El usario fue reactivado")
        
        
#Permitir la actualización de la contraseña de acceso al sistema.
    def actualizar_contrasenia(self, contrasenia_nueva):
        self.__contrasenia = contrasenia_nueva



