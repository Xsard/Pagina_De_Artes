import pymysql
from Artistas import Artista

def connection():
    try:
        conn = pymysql.connect(host='localhost', user='root',password='',db='artspace')
    except:
        print("Error de conexion")
    return conn

def insert(artista):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            nonQuery = "INSERT INTO USERS(EMAIL, CONTRASEÑA) VALUES (%s,PASSWORD(%s))"
            cursor.execute(nonQuery,(artista.email, artista.contraseña))
            nonQuery = "INSERT INTO ARTISTA(ID_ARTISTA, NOMBRE, APATERNO, AMATERNO, NOMBRE_ARTISTICO, FECHA_NAC, EMAIL_CONTACTO, ID_CIUDAD, EMAIL) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(nonQuery,('NULL', artista.nombre, artista.apaterno, artista.amaterno, artista.nombreArt, artista.fecha_Nac, artista.email_contacto, artista.ciudad, artista.email))
        conn.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrió un error a la hora de insertar",e)
    conn.close()

def selectWhere(email, password):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            query = "SELECT ART.ID_ARTISTA FROM ARTISTA ART JOIN USERS USR ON(ART.EMAIL = USR.EMAIL) WHERE USR.EMAIL = %s AND USR.CONTRASEÑA=PASSWORD(%s)"
            if cursor.execute(query,(email,password))>0:
                data = cursor.fetchall()
                return data
            else:
                query = "SELECT ADMIN.ID_ADMIN FROM ADMINISTRADOR ADMIN JOIN USERS USR ON(ADMIN.EMAIL = USR.EMAIL) WHERE USR.EMAIL = %s AND USR.CONTRASEÑA=PASSWORD(%s)"
                if cursor.execute(query,(email,password))>0:
                    data = cursor.fetchall()
                    return data
                else:
                    return -1
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error",e)
    conn.close()