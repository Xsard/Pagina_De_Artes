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

#Listado de países
def selectAll():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM PAIS")
            data = cursor.fetchall()
            return data
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()

def deleteWhere(cod):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery="DELETE FROM PAIS WHERE ID_PAIS = %s;"
            cursor.execute(nonQuery, (cod))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()

def update(cod,nom):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery="UPDATE PAIS SET NOMBRE_PAIS=%s WHERE ID_PAIS=%s"
            cursor.execute(nonQuery,(nom,cod))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
                print("Error",e)
    conn.close()
