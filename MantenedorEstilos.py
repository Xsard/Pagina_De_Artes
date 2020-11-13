import pymysql
from Estilos import Estilo

#Conexión a la base de datos
def connection():
    try:
        conn = pymysql.connect(host='localhost', user='root',password='',db='artspace')
    except:
        print("Error de conexion")
    return conn

#Insertar un país
def insert(estilo):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery = "INSERT INTO ESTILO(COD_ESTILO, NOMBRE, DESCRIPCION) VALUES (%s,%s,%s)"
            cursor.execute(nonQuery,(estilo.codigo,estilo.nombre,estilo.descripcion))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error a la hora de insertar",e)
    conn.close()