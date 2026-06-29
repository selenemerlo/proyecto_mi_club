from encapsulamiento.ejercicio1.club import Club

class ClubCategoria(Club):
    def __init__(self,  nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__( nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.activiades = []

    def mostrar_datos2 (self):
        for i in self.activiades:
            print(i)

    def agregar_socio(self, socio):
        self.__socios.append(socio)

    def agregar_actividades(self, actividad):
        self.activiades.append(actividad)

    def mostrar_socios(self):
        for i in self.__socios:
            print(i)

    def get_socios(self):
        return self.__socios
    def set_socios(self, socios_modificado):
        self.__socios = socios_modificado

