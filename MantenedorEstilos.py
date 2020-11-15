import pymysql
from Estilos import Estilo

#Conexión a la base de datos
def connection():
    try:
        conn = pymysql.connect(host='localhost', user='root',password='',db='artspace')
    except:
        print("Error de conexion")
    return conn

#Insertar un Estilo
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

#Listado de Estilo
def selectAll():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM ESTILO")
            data = cursor.fetchall()
            return data
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()

#Eliminar Estilo
def deleteWhere(cod):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery="DELETE FROM ESTILO WHERE COD_ESTILO = %s;"
            cursor.execute(nonQuery, (cod))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()

#Actualizar Estilo
def update(cod,nom):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery="UPDATE ESTILO SET NOMBRE_ESTILO=%s WHERE COD_ESTILO=%s"
            cursor.execute(nonQuery,(nom,cod))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
                print("Error",e)
    conn.close()    