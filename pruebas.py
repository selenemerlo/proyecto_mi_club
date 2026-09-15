from datetime import date
from pathlib import Path
from base_datos.base_datos import conectar, crear_tablas, guardar_socio
from modelo.socio import Socio

RUTA = Path(__file__).parent / "club.db"

conexion = conectar(str(RUTA))
crear_tablas(conexion)

# Ahora pasamos los 10 argumentos requeridos (incluyendo el parámetro 'rol')
Yair = Socio(
    "Yair ALderete ", 
    16, 
    "DNI", 
    "50068726", 
    "Argentina",
    date(2026, 8, 6), 
    "Activo", 
    "chaos", 
    "goku123",
    "socio" # <-- Faltaba definir el rol
)

guardar_socio(conexion, Yair)
print("Socio guardado correctamente en la base de datos.")

