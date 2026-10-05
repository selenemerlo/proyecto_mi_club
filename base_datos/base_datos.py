import sqlite3
from datetime import date
from modelo.cuota import Cuotas
from modelo.socio import Socio
from modelo.club import Club


def conectar(ruta):
    """Abre una conexión a la base de datos en la ruta indicada.
    Si el archivo no existe, lo crea automáticamente."""
    conexion = sqlite3.connect(ruta)
    return conexion

def crear_tablas(conexion):
    """Crea las tablas necesarias si no existen."""
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo     TEXT NOT NULL,
            edad                INTEGER,
            tipo_identificacion TEXT,
            identificacion      TEXT,
            nacionalidad        TEXT,
            fecha_inscripcion   TEXT,
            estado              TEXT DEFAULT 'Activo',
            rol                 TEXT DEFAULT 'socio',
            usuario             TEXT UNIQUE NOT NULL,
            contrasenia         TEXT NOT NULL
        )
    """)
    conexion.commit()

    """Crea las tablas necesarias si no existen."""
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuotas (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            socio_id  INTEGER NOT NULL,
            estado TEXT DEFAULT 'pendiente',
            fecha_de_vencimiento TEXT,
            periodo TEXT NOT NULL
        )
    """)
    conexion.commit()
    """Crea las tablas necesarias si no existen."""
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubes (
            club_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            ubicacion TEXT NOT NULL,
            presidente TEXT NOT NULL,
            fecha_fundacion TEXT
        )
    """)
    conexion.commit()

    cursor.conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS socio_actividad (
        socio_id     INTEGER,
        actividad_id INTEGER,
        PRIMARY KEY (socio_id, actividad_id),
        FOREIGN KEY (socio_id) REFERENCES socios(id),
        FOREIGN KEY (actividad_id) REFERENCES actividades(id)
    )
""")



def guardar_socio(conexion, socio):
    """Recibe un objeto Socio y lo guarda en la tabla socios."""
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO socios (nombre_completo, edad, tipo_identificacion,
                            identificacion, nacionalidad, fecha_inscripcion,
                            estado, rol, usuario, contrasenia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        socio.nombre_completo,
        socio.edad,
        socio.get_tipo_identificacion(),
        socio.get_identificacion(),
        socio.get_nacionalidad(),
        socio.fecha_inscripcion.isoformat(),
        socio.estado,
        socio.rol,
        socio.get_usuario(),
        socio.get_contrasenia()
    ))
    conexion.commit()



def guardar_cuota(conexion, socio, cuota):
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (socio.get_usuario(),))
    fila = cursor.fetchone()
    if fila is None:
        raise ValueError("El socio no existe")

    socio_id = fila[0]

    cursor.execute("""
        INSERT INTO cuotas (socio_id, estado, fecha_de_vencimiento, periodo)
        VALUES (?, ?, ?, ?)
    """, (
        socio_id,
        cuota.get_estado(),
        cuota.fecha_de_vencimiento,
        cuota.periodo
    ))
    conexion.commit()



def listar_cuotas_de_socio(conexion, usuario):
    """Devuelve una lista de objetos Cuota para el socio con ese usuario."""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return []

    socio_id = fila[0]

        # Traer todas las cuotas de ese socio
    cursor.execute(
        "SELECT periodo, estado, fecha_vencimiento FROM cuotas WHERE socio_id = ?",
        (socio_id,)
    )

    cuotas = []
    for periodo, estado, fecha_vencimiento in cursor.fetchall():
        cuota = Cuotas(estado, date.fromisoformat(fecha_vencimiento), periodo)
        cuotas.append(cuota)
    return cuotas


#buscar un socio

def buscar_socio_por_usuario(conexion, usuario):
    """Devuelve el Socio (con sus cuotas cargadas) o None si no existe."""
    cursor = conexion.cursor()
    cursor.execute("""SELECT * FROM socios WHERE usuario = ? """, (usuario,) )
    fila = cursor.fetchone()
    if fila is None:
        return None
    else:
        return construir_socio()

def construir_socio(fila):
    (nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, fecha_inscripcion, estado, rol, usuario, contrasenia) = fila
    return Socio(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, fecha_inscripcion, estado, rol, usuario, contrasenia)


#guardar club
def guardar_club(conexion, clubes):
    """Guarda el club en la tabla clubes (solo si no existe uno)."""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM clubes")
    fila = cursor.fetchone()
    if fila is not None:
        return fila[0]

    cursor.execute(
        "INSERT INTO clubes (nombre, descripcion,ubicacion, presidente, fecha_fundacion) VALUES (?, ?, ?, ?, ?)", 
        (
        clubes.nombre,
        clubes.descripcion,
        clubes.ubicacion,
        clubes.get.presidente(),
        clubes.get.fecha_de_fundacion()
        ))
    conexion.commit()


