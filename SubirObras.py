import pymysql
from Obras import Obra

#Conexión a la base de datos
def connection():
    try:
        conn = pymysql.connect(host='localhost', user='root',password='',db='artspace')
    except:
        print("Error de conexion")
    return conn

#Insertar una Obra
def insert(obra, img):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery = "INSERT INTO OBRA(NOMBRE_OBRA, DESC_OBRA, COD_ESTILO, ID_ARTISTA) VALUES (%s,%s,%s,%s)"
            cursor.execute(nonQuery,(obra.Nombre, obra.Desc, obra.Estilo, obra.ID_Artista))
            nonQuery = "INSERT INTO IMG_OBRA(COD_OBRA, PATH) VALUES (%s,%s)"
            cursor.execute(nonQuery,(1, img))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error a la hora de insertar",e)
    conn.close()