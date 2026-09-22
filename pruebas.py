from datetime import date
from pathlib import Path
from base_datos.base_datos import conectar, crear_tablas, guardar_socio, guardar_cuota
from modelo.socio import Socio
from modelo.cuota import Cuotas

RUTA = Path(__file__).parent / "club.db"

conexion = conectar(str(RUTA))
crear_tablas(conexion)

# Ahora pasamos los 10 argumentos requeridos (incluyendo el parámetro 'rol')
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