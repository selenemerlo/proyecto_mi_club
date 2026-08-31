from persona import Persona
from datetime import date, timedelta

class Socio(Persona):
    def __init__(self,nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad,fecha_inscripcion, estado, usuario, contrasenia):
        super().__init__(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad)
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

    def set_contrasenia(self, contrasenia_nueva):
        self.__contrasenia = contrasenia_nueva
    def get_contrasenia(self):
        return self.__contrasenia


    
#1-Permitir que un socio pueda asociarse a uno o más clubes.
    def asociarse_club(self, club):
        if club not in self.lista_clubes:
            self.lista_clubes.append(club)
            print("Socio asociado al club correctamente.")
        else:
            print("El socio ya está asociado a ese club.")
          


#2-Permitir que un socio deje de pertenecer a un club determinado.
    def eliminar_de_club(self, nombre):
        for socio in self.lista_clubes:
            if socio == nombre:
                self.lista_clubes.remove(nombre)
                print("El socio dejo de pertenecer a este club")
            else:
                print("El socio no esta en la lista")



#3-Generar nuevas cuotas correspondientes a distintos períodos.
    def generar_cuotas(self):
        fecha_actual = date.today()
        fecha_vencimiento = fecha_actual + timedelta(days=30)

        nueva_cuota = {
            "fecha_actual": fecha_actual,
            "fecha_vencimiento": fecha_vencimiento,
            "pendiente": True
        }

        self.lista_cuotas.append(nueva_cuota)
        print(f"Cuota generada. Vence el {fecha_vencimiento}.")



#4-Registrar el pago de una cuota pendiente.

    def registrar_pago_cuota(self):
        for cuota in self.lista_cuotas:
            if cuota == "pendiente":
                cuota = "pagada"
                print("La cuota se pago correctamente")
            else:
                print("No hay cuotas pendientes")



#5-Informar si el socio posee deudas o cuotas sin abonar.

    def tiene_deudas(self):
        if len(self.lista_cuotas) > 0:
            print("El socio posee cuotas sin abonar.")
        else:
            print("El socio no posee deudas registradas.")



#6-Mostrar la cantidad de cuotas pendientes de pago.

    def mostrar_cuotas_pendientes(self):
        cantidad = 0
        for cuota in self.lista_cuotas:
            if cuota == "pendiente":
                cantidad += 1
            print(f"El socio tiene {cantidad} cuotas pendientes")



#7-Cambiar el estado de un socio activo a suspendido cuando corresponda.
    def estado_socio(self):
        if self.estado == "activo":
                self.estado = "suspendido"
                print("El usuario ha sido suspendido")
        else:
            print("El usuario sigue activo")



#8-Reactivar un socio suspendido para que pueda volver a utilizar los servicios del club.

    def reactivar_socio(self):
        if self.estado == "suspendido":
            self.estado = "activo"
            print("El usario fue reactivado")
        
        
#9-Permitir la actualización de la contraseña de acceso al sistema.
    def actualizar_contrasenia(self, contrasenia_nueva):
        self.__contrasenia = contrasenia_nueva



#10-Verificar los datos de acceso ingresados por el socio al momento de iniciar sesión.

    def verificar_acceso(self, usuario_ingresado, contrasenia_ingresada):
        if self.get_usuario() == usuario_ingresado and self.get_contrasenia() == contrasenia_ingresada:
            print("Acceso concedido.")
        else:
            print("Usuario o contraseña incorrectos.")



sociocito = Socio("Ezequiel",28,"DNI", "48876982","Argentino","12/05/2024","activo","welco","goku123")
#1
sociocito.verificar_acceso("welco", "goku123")
#2
sociocito.asociarse_club("San Lorenzo")
#3
sociocito.eliminar_de_club("Ezequiel")
#4
sociocito.generar_cuotas()
#5
sociocito.registrar_pago_cuota()
#6
sociocito.tiene_deudas()
#7
sociocito.mostrar_cuotas_pendientes()
#8
sociocito.estado_socio()
#9
sociocito.reactivar_socio()
#10
sociocito.set_contrasenia("123456")




