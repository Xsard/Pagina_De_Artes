import pymysql
from Ciudades import Ciudad

#Conexión a la base de datos
def connection():
    try:
        conn = pymysql.connect(host='localhost', user='root',password='',db='artspace')
    except:
        print("Error de conexion")
    return conn

#Insertar una Ciudad
def insert(ciudad):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery = "INSERT INTO CIUDAD(ID_CIUDAD, NOMBRE_CIUDAD, ID_PAIS) VALUES (%s,%s,%s)"
            cursor.execute(nonQuery,(ciudad.codigo,ciudad.nombre,ciudad.idpais))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error a la hora de insertar",e)
    conn.close()

#Listado de Ciudad
def selectAll():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM CIUDAD")
            data = cursor.fetchall()
            return data
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()

#Eliminar Ciudad
def deleteWhere(cod):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery="DELETE FROM CIUDAD WHERE ID_CIUDAD = %s;"
            cursor.execute(nonQuery, (cod))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()

#Actualizar Ciudad
def update(cod,nom):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery="UPDATE CIUDAD SET NOMBRE_CIUDAD=%s WHERE ID_CIUDAD=%s"
            cursor.execute(nonQuery,(nom,cod))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
                print("Error",e)
    conn.close()    