import pymysql
from Administradores import Administrador

#Conexión a la base de datos
def connection():
    try:
        conn = pymysql.connect(host='localhost', user='root',password='',db='artspace')
    except:
        print("Error de conexion")
    return conn

#Insertar una Administrador
def insert(administrador):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery = "INSERT INTO USERS(EMAIL, CONTRASEÑA) VALUES (%s,PASSWORD(%s))"
            cursor.execute(nonQuery,(administrador.email, administrador.password))
            nonQuery = "INSERT INTO ADMINISTRADOR(ID_ADMIN, NOMBRE, APATERNO, AMATERNO, EMAIL) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(nonQuery,('NULL', administrador.nombre, administrador.apellidoPaterno, administrador.apellidoMaterno, administrador.email))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error a la hora de insertar",e)
    conn.close()

#Listado de Administrador
def selectAll():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM ADMINISTRADOR")
            data = cursor.fetchall()
            return data
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()

#Eliminar Administrador
def deleteWhere(cod):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery="DELETE FROM ADMINISTRADOR WHERE ID_ADMIN = %s;"
            cursor.execute(nonQuery, (cod))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()

#Actualizar Administrador
def update(cod,nom,aPaterno,aMaterno,email):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery="UPDATE ADMINISTRADOR SET NOMBRE=%s, APATERNO=%s, AMATERNO=%s, EMAIL=%s WHERE ID_ADMIN=%s"
            cursor.execute(nonQuery,(nom,aPaterno,aMaterno,email,cod))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
                print("Error",e)
    conn.close()

deleteWhere(1)