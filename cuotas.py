from datetime import datetime

class Cuotas:
    def __init__(self, estado, fecha_de_vencimiento, periodo):
        self.__estado = estado
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.periodo = periodo

    def set_estado (self, estado_modificado):
        self.__estado = estado_modificado
    def get_estado (self):
        return self.__estado

        

#1-Registrar una cuota como pagada.
    def registrar_pago(self):
        self.__estado = "pagado"
        print("La cuota fue pagada correctamente")

#2-Determinar si una cuota se encuentra vencida comparando la fecha de vencimiento con la fecha actual.

    def actualizar_estado(self):
        self.__estado != "pagado" and datetime.now()> self.fecha_de_vencimiento
        self.estado = "Vencida"
        print("La cuota esta vencida")


#3-Actualizar automáticamente el estado de la cuota cuando corresponda.

    def cuota_nueva(self,estado_nuevo):
        self.__estado = estado_nuevo


#4-Informar cuántos días faltan para el vencimiento de una cuota.  

    def dias_faltantes(self):
        ahora = datetime.now()

        if ahora > self.fecha_de_vencimiento:
            print("La cuota ya se vencio")
        diferencia = self.fecha_de_vencimiento - ahora
        print("faltan:", diferencia,"dias para el vencimiento de la cuota")

#5-Permitir la renovación de una cuota para un nuevo período.

    def renovar_cuota(self, nuevo_periodo):
        self.periodo = nuevo_periodo




cuotita = Cuotas("activo","12/10/2026","mensual")
#1
cuotita.registrar_pago()
#2
cuotita.actualizar_estado()
#3
print(cuotita.get_estado())
#4
cuotita.dias_faltantes()#no anda
#5
print(cuotita.renovar_cuota())
