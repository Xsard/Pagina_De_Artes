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
            nonQuery = "INSERT INTO OBRA(COD_OBRA ,NOMBRE_OBRA, DESC_OBRA, PRECIO_INICIAL, FECHA_TERMINO_SUBASTA, COD_ESTILO, ID_ARTISTA) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(nonQuery,(obra.CodObra, obra.Nombre, obra.Desc, obra.Precio, obra.Fecha_Ter, obra.Estilo, obra.ID_Artista))
            nonQuery = "INSERT INTO IMG_OBRA(COD_OBRA, PATH) VALUES (%s,%s)"
            cursor.execute(nonQuery,(obra.CodObra, img))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error a la hora de insertar",e)
    conn.close()

def select():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT ART.NOMBRE, OBR.NOMBRE_OBRA, OBR.DESC_OBRA, OBR.PRECIO_INICIAL, OBR.FECHA_TERMINO_SUBASTA, IMO.PATH, NVL((SELECT MAX(VALOR_PUJA) FROM subasta SUB WHERE SUB.COD_OBRA=OBR.COD_OBRA),0), OBR.COD_OBRA FROM OBRA OBR JOIN IMG_OBRA IMO ON (OBR.COD_OBRA=IMO.COD_OBRA) JOIN ARTISTA ART ON (OBR.ID_ARTISTA=ART.ID_ARTISTA)")
            data = cursor.fetchall()
            return data
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()
