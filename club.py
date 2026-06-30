class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.__presidente = presidente #atributo privado
        self.__fecha_fundacion = fecha_fundacion #atributo privado

    
    def mostrar_info (self):
        return f'El nombre del club es {self.nombre},{self.descripcion}, esta ubicado en {self.ubicacion},el presidente del club es {self.__presidente}, y el club fue fundado en {self.__fecha_fundacion}'
    

    #get y set de presidente
    def get_presidente(self):#devuelve el valor
        return self.__presidente
    def set_presidente(self, presidente_modificado):#modifica el valor
        self.__presidente = presidente_modificado

    #get y set de  fundacion
    def get_fecha(self):
        return self.__fecha_fundacion
    def set_fecha(self, fecha_modificada):
        self.__fecha_fundacion = fecha_modificada

#nuevos metodos 30/6/26

    def modificar_presidente(self,autoridades):
        if autoridades != autoridades:
            print("el presi a cambiado")

    def antigüedad(self):
        if self.__fecha_fundacion>50:
            print("Es una institución histórica")
        else:
            print("Le faltan unos años más para ser histórica")