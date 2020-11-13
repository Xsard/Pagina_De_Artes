import pymysql
from Paises import Pais

#Conexión a la base de datos
def connection():
    try:
        conn = pymysql.connect(host='localhost', user='root',password='',db='artspace')
    except:
        print("Error de conexion")
    return conn

#Insertar un país
def insert(pais):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery = "INSERT INTO PAIS(ID_PAIS, NOMBRE_PAIS) VALUES (%s,%s)"
            cursor.execute(nonQuery,(pais.codigo,pais.nombre))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error a la hora de insertar",e)
    conn.close()