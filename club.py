from datetime import datetime

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
    def set_presidente(self, presidente_modificado):#modifica el valor
        self.__presidente = presidente_modificado
    def get_presidente(self):#devuelve el valor
        return self.__presidente


    #get y set de  fundacion
    def get_fecha(self):
        return self.__fecha_fundacion
    def set_fecha(self, fecha_modificada):
        self.__fecha_fundacion = fecha_modificada

#1-Permitir modificar el presidente del club cuando se produzca un cambio de autoridades.

    def cambiar_presidente(self, presidente_modificado):
        presidente = presidente_modificado
        

#2-Mostrar la antigüedad del club calculando los años transcurridos desde su fecha de fundación hasta la fecha actual.

    def mostrar_antiguedad(self):
        hoy = datetime.today()
        fecha_obj = datetime.strptime(self.get_fecha(), "%d/%m/%Y").date()#el strtime 
        antiguedad = hoy.year - fecha_obj

        # Ajustamos si todavía no cumplió años en el año actual
        if (hoy.month, hoy.day) < ( fecha_obj.month, fecha_obj.day,):
            antiguedad -= 1

        print (f"La antigüedad del club {self.nombre} es de {antiguedad} años.")



#3-Determinar si el club puede considerarse una institución histórica, entendiendo como tal a aquellas que tengan más de 50 años de existencia.

    def antiguedad(self):
        antiguedad = datetime.now().year - self.get_fecha()
        if antiguedad > 50:
            print("El club es historico")
        else:
            print("El club no es historico")




boca = Club("Boca Juniors","Xeneizes", "La boca", "Riquelme","03/04/1905")
#1
boca.set_presidente("Macri")
print(boca.get_presidente())
#2
boca.mostrar_antiguedad()