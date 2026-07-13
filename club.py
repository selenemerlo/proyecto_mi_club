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

#Permitir modificar el presidente del club cuando se produzca un cambio de autoridades.

    def cambiar_presidente(self, presidente_modificado):
        presidente = presidente_modificado


#Determinar si el club puede considerarse una institución histórica, entendiendo como tal a aquellas que tengan más de 50 años de existencia.


from datetime import datetime


anio_fundacion = 1903
antiguedad = datetime.now().year - anio_fundacion

if antiguedad > 50:
    print("El club es historico")
else:
    print("El club no es historico")


calc = 2026
calc2 = 50

print(calc- calc2)