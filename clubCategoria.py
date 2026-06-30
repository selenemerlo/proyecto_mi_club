from club import Club

class ClubCategoria(Club):
    def __init__(self,  nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__( nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.activiades = []

    def get_socios(self):
        return self.__socios

    def set_socios(self, socios_modificado):
        self.__socios = socios_modificado

#metodos nuevos 29/6/26
    
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

    def registrar_socios(self,registrado):
        self.__socios.append(registrado)


    def cantidad_socios_reg(self):
        for i in self.__socios.__len__:
            print("La cantidad de socios registrados son: ",i)

#metodos nuevos 30/6/26

    def agregar_actividades(self,actividad_nueva):
        self.__socios.append(actividad_nueva)

    def mostrar_actividades(self):
        print(f"Las actividades son: ",self.activiades)
    
    def eliminar_socios(self,socio_no_registrado):
        self.__socios.pop(socio_no_registrado)

    def buscar_socios(self,Enrique):
        for i in self.__socios:
            if i == Enrique:
                print("Socio encontrado")
                

    def eliminar_actividades(self,actividad_no_disponible):
        for i in self.activiades:
            if i == actividad_no_disponible:
                print("La actividad no se encuentra disponible temporalmente")


    def porcentaje_socios(self,socios_registrados_activos):
        for i in self.__socios:
            if self.__socios == socios_registrados_activos:
                print(self.__socios/socios_registrados_activos*1000)