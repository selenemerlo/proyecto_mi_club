from clubCategoria import ClubCategoria
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

#1-Registrar nuevos socios en un club.
    def registrar_socios(self, club_categoria, nombre_socio, activo=True):
        """
        Registra un nuevo socio dentro de la categoría del club indicada.
        club_categoria: instancia de ClubCategoria
        """
        return ClubCategoria.registrar_socio(nombre_socio, activo)
        
#2-Suspender socios cuando incumplan alguna normativa o mantengan deudas pendientes.
    def suspender_socios(self, club_categoria, nombre_socio, motivo=""):
        """Suspende a un socio de una categoría del club cuando incumple normativa o tiene deudas pendientes."""
        suspendido = ClubCategoria.suspender_socio(nombre_socio)
        if suspendido:
            print(f"Socio '{nombre_socio}' suspendido correctamente. Motivo: {motivo or 'no especificado'}")
        else:
            print(f"No se encontró al socio '{nombre_socio}' en esta categoría.")
        return suspendido


#3-Reactivar socios previamente suspendidos.
    def reactivar_socio(self):
        if self.__usuario == "supendido":
            self.__usuario = "reactivado"
            print("El usuario a sido reactivado")



#4-Obtener un listado completo de los socios pertenecientes a un club.
    def listar_socios(self, club_categoria):
        socios = ClubCategoria.mostrar_socios()
        if not socios:
            print(f"La categoría '{ClubCategoria.nombre}' no tiene socios registrados.")
            return socios


#5-Verificar las credenciales de acceso del administrador.

    def verificar_credenciales(self, usuario, contrasenia):
        if self.__usuario == usuario and self.__contrasenia == contrasenia:
            print("Acceso concedido.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False
        

