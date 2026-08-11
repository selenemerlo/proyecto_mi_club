from clubCategoria import ClubCategoria
class Administrador(ClubCategoria):
    def __init__(self,nombre_admin, usuario, contrasenia,nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.nombre_admin = nombre_admin
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
    def registrar_socios(self, nombre_socio, activo=True):
        return self.registrar_socio(nombre_socio, activo)
        
#2-Suspender socios cuando incumplan alguna normativa o mantengan deudas pendientes.
    def suspender_socios(self, nombre_socio):
        suspendido = self.suspender_socio(nombre_socio)
        if suspendido:
            print(f"Socio '{nombre_socio}' suspendido correctamente.")
        else:
            print(f"No se encontró al socio '{nombre_socio}' en esta categoría.")
        return suspendido


#3-Reactivar socios previamente suspendidos.
    def reactivar_socio(self, nombre):
        for socio in self.__socios:
            if socio["nombre"] == nombre:
                socio["activo"] = True
                print(f"El socio {nombre}, fue reactivado")
        print(f"El socio {nombre}, ya estaba acivo")



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
        



sociocito = Administrador("selene", "sel_yaz", "goku123", "Boca Juniors","Xeneizes", "La boca", "Riquelme","03/04/1905")
sociocito.registrar_socios("selene")
print(sociocito.suspender_socio("selene"))
sociocito.reactivar_socio("selene")