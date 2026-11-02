from datetime import date
from pathlib import Path
from base_datos.base_datos import conectar, crear_tablas, guardar_socio, buscar_socio_por_usuario, guardar_cuota, listar_cuotas_de_socio, guardar_club, guardar_actividad, anotar_socio_actividad, listar_actividades_de_socio, desanotar_socio_actividad
from modelo.socio import Socio
from modelo.cuota import Cuota
from modelo.club import Club
from modelo.actividades import Actividad

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
    "socio",
    "bubu", 
    "ezebubu"
     # <-- Faltaba definir el rol
)


yair = Socio(
    "Yair Alderete ", 
    16, 
    "DNI", 
    "50128463", 
    "Argentina",
    date(2024, 11, 23), 
    "Activo",
    "socio" , 
    "chaos", 
    "yair123"
    
)

guardar_socio(conexion, Bubu)
guardar_socio(conexion, yair)
buscar_socio_por_usuario(conexion, "chaos")
print("se busco el socio")
#-------------------------------------------------------------------------------------------------#

RUTA = Path(__file__).parent / "club.db"

conexion = conectar(str(RUTA))
crear_tablas(conexion)

cuota1 = Cuota(
    "pendiente",
    date(2026,5,12),
    "25"
)

guardar_cuota(conexion,Bubu, cuota1)
print("cuota guardada correctamente ")


#------------------------------------------------------------------------------------------------___#

clubcito = Club(
        "Boca Juniors",
        "Club de futbol",
        "La Boca",
        "Macri",
        "3 de abril de 1905"
)
guardar_club(clubcito)
conexion.close()