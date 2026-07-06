class Cuotas:
    def __init__(self, estado, fecha_de_vencimiento, periodo):
        self.__estado = estado
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.periodo = periodo


    def get_estado (self):
        return self.__estado
    def set_estado (self, estado_modificado):
        self.__estado = estado_modificado
        




#Actualizar automáticamente el estado de la cuota cuando corresponda.

    def cuota_nueva(self,estado_nuevo):
        self.__estado = estado_nuevo


#Permitir la renovación de una cuota para un nuevo período.

    def cuota_renovada(self, periodo_nuevo):
        self.periodo = periodo_nuevo

