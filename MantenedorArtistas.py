import pymysql
from Artistas import Artista

#Conexión a la base de datos
def connection():
    try:
        conn = pymysql.connect(host='localhost', user='root',password='',db='artspace')
    except:
        print("Error de conexion")
    return conn

#Insertar una Ciudad
def insert(artista):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery = "INSERT INTO ARTISTA(ID_CIUDAD,ID_ARTISTA, EMAIL_NEGOCIOS, NOMBRES, NOMBRE_ARTISTICO, EDAD, EMAIL) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(nonQuery,(artista.codigoCiudad,artista.codigo,artista.nombres,artista.emailNegocios,artista.nombreArtistico,artista.edad,artista.email))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error a la hora de insertar",e)
    conn.close()