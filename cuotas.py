class Cuotas:
    def __init__(self, estado, fecha_de_vencimiento, periodo):
        self.__estado = estado
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.periodo = periodo


    def get_estado (self):
        return self.__estado
    def set_estado (self, estado_modificado):
        self.__estado = estado_modificado
        