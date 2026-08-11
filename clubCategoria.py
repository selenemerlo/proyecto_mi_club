from club import Club

class ClubCategoria(Club):
    def __init__(self,  nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__( nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.activiades = []

    def mostrar_datos2 (self):
        for i in self.activiades:
            print(i)

    def agregar_actividades(self, actividad):
        self.activiades.append(actividad)


    def mostrar_socios(self):
        for i in self.__socios:
            print(i)

    def get_socios(self):
        return self.__socios
    def set_socios(self, socios_modificado):
        self.__socios = socios_modificado



#1-Incorporar la funcionalidad para registrar nuevos socios dentro de la categoría correspondiente.

    def registrar_socio(self, nombre, activo = True):
        socio = {"nombre" : nombre, "activo": activo}
        self.__socios.append(socio)
        print(f"Socio {socio['nombre']} registrado correctamente")


#2-Permitir eliminar socios de la categoría cuando estos dejen de pertenecer a ella.
    def eliminar_socios(self, nombre): # eliminar el socio por el nombre
        for socio in self.__socios:
            if socio["nombre"] == nombre:
                self.__socios.remove(socio)
                print("El socio fue eliminado correctamente ")
            else:
                print("El socio no fue encontrado")
        
#3-Implementar una búsqueda que permita localizar rápidamente un socio utilizando algún dato identificatorio.

    def buscar_socio(self, nombre): # buscar el socio por el nombre
        for socio in self.__socios:
            if socio["nombre"] == nombre:
                self.__socios.index(socio)
                print("Socio encontrado")
            else:
                print("El socio no fue encontrado")


#4-Obtener la cantidad total de socios registrados en la categoría.
    def cantidad_socios(self):
        print("la cantidad de socios es: ", len(self.__socios))

#5-Permitir agregar nuevas actividades deportivas, recreativas o culturales ofrecidas por el club.
    def agregar_actividad(self, actividad):
        self.activiades.append(actividad)



#6-Permitir eliminar actividades que ya no se encuentren disponibles.
    def eliminar_actividad(self, actividad):
        self.activiades.remove(actividad)


#7-Mostrar un listado completo de las actividades que se realizan en la categoría.
    def listado_actividades(self):
        for i in self.activiades:
            print(i)


#8-Calcular qué porcentaje de los socios registrados se encuentra actualmente en estado activo.

    def porcentaje_socios_activos(self):
        socios = self.get_socios()
        activos = 0
        for socio in socios:
            if socio["activo"] == True:
                activos += 1  
        porcentaje = (activos / len(socios)) * 100
        return round(porcentaje, 2)
    

 # Método de apoyo para poder suspender desde afuera sin exponer __socios
    def suspender_socio(self, nombre):
        for socio in self.__socios:
            if socio["nombre"] == nombre:
                socio["activo"] = False
                print(f"El socio {nombre}, esta suspendido")
        print(f"El socio {nombre}, ya estaba suspendido")
    

boca = ClubCategoria("Boca Juniors","Xeneizes", "La boca", "Riquelme","03/04/1905")
boca.registrar_socio("Selene")
boca.registrar_socio("Martin")
boca.registrar_socio("Isaias")
boca.registrar_socio("Chango")
boca.registrar_socio("Bubu")

boca.suspender_socio("Bubu")

print(boca.porcentaje_socios_activos())
boca.mostrar_info()
