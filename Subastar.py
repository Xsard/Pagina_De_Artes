import pymysql
from Subastas import Subasta

#Conexión a la base de datos
def connection():
    try:
        conn = pymysql.connect(host='localhost', user='root',password='',db='artspace')
    except:
        print("Error de conexion")
    return conn

def insert(subasta):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            if select(subasta.CodObra, subasta.CodArtista):
                nonQuery = "INSERT INTO SUBASTA VALUES(%s,%s,%s)"
                cursor.execute(nonQuery,(subasta.CodObra, subasta.CodArtista, subasta.Precio))
            else:
                nonQuery = "UPDATE SUBASTA SET VALOR_PUJA = %s WHERE COD_OBRA = %s AND ID_ARTISTA = %s"
                cursor.execute(nonQuery,(subasta.Precio, subasta.CodObra, subasta.CodArtista))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error a la hora de insertar",e)
    conn.close()

def select(obra, usuario):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM SUBASTA WHERE COD_OBRA = %s AND ID_ARTISTA = %s"
            if cursor.execute(query,(obra,usuario))>0:            
                return False
            else:
                return True
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error: ",e)
    conn.close()

