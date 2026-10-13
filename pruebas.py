from datetime import date
from pathlib import Path
from base_datos.base_datos import conectar, crear_tablas, guardar_cuota, buscar_socio_por_usuario, guardar_actividad ,guardar_socio
from modelo.socio import Socio
from modelo.cuota import Cuotas
from modelo.club import Club

RUTA = Path(__file__).parent / "club.db"

conexion = conectar(str(RUTA))
crear_tablas(conexion)

# Ahora pasamos los 10 argumentos requeridos (incluyendo el parámetro 'rol')
#el socio ya esta guardado
Bubu = Socio(
    "Ezequiel Vitullo ", 
    28, 
    "DNI", 
    "45908376", 
    "Argentina",
    date(2024, 11, 23), 
    "Activo", 
    "bubu", 
    "ezebubu",
    "socio" # <-- Faltaba definir el rol
)

yair = Socio(
    "Yair Alderete ", 
    16, 
    "DNI", 
    "50128463", 
    "Argentina",
    date(2024, 11, 23), 
    "Activo", 
    "chaos", 
    "yair123",
    "socio" 
)

# guardar_socio(conexion, Bubu)
# guardar_socio(conexion, yair)
buscar_socio_por_usuario(conexion, "chaos")
print("se busco el socio")
#-------------------------------------------------------------------------------------------------#

RUTA = Path(__file__).parent / "club.db"

conexion = conectar(str(RUTA))
crear_tablas(conexion)

cuota1 = Cuotas(
    "pendiente",
    date(2026,5,12),
    "25"
)

guardar_cuota(conexion,Bubu, cuota1)
print("cuota guardada correctamente ")


#------------------------------------------------------------------------------------------------___#
#club se guarda automaticamente
clubcito = Club(
        "Boca Juniors",
        "Club de futbol",
        "La Boca",
        "Macri",
        "3 de abril de 1905"
)

conexion.close()