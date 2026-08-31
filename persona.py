class Persona:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad

    

    
    def get_tipo_identificacion(self):
        return self.__tipo_identificacion
    def set_tipo_identificacion(self, tipo_identificacion_modificada):
        self.__tipo_identificacion = tipo_identificacion_modificada

    def get_identificacion(self):
        return self.__identificacion
    def set_identifacion(self, identificacion_modificada):
        self.__identificacion = identificacion_modificada

    def get_nacionalidad(self):
        return self.__nacionalidad
    def set_nacionalidad(self, nacionalidad_modificada):
        self.__nacionalidad = nacionalidad_modificada

    def mostrar_datos(self):
        return f'nombre:{self.nombre_completo}, edad de la persona:{self.edad}, tipo de identicacion: {self.get_tipo_identificacion()}, identifacion:{self.get_identificacion()}, nacionalidad{self.get_nacionalidad()}'




#1-Determinar automáticamente si una persona es mayor o menor de edad.
    def edad_persona(self):
        if self.edad >= 18:
            print(f"{self.nombre_completo} es mayor de edad")

        else:
            print(f"{self.nombre_completo} es menor de edad")



#2-Verificar que la identificación ingresada sea válida y no se encuentre vacía.

    def identificacion_valida(self):
        if len(self.get_identificacion())>=7 and len(self.get_identificacion())<= 8:
            print("La identificacion ingresada es valida")
        else:
            print("La identificacion ingresada no es valida")
            


selene = Persona("Selene Yazmin Merlo",16, "DNI","50453246","Argentina")
#1
selene.edad_persona()
#2
selene.identificacion_valida()