import os
from flask import Flask, render_template, request, flash, redirect, url_for, session
import Paises, MantenedorPaises
import Ciudades, MantenedorCiudades
import Estilos, MantenedorEstilos
import Administradores, MantenedorAdministradores
import Artistas, RegistroUsuarios
import Obras, SubirObras
import Subastas, Subastar
from werkzeug.utils import secure_filename
from datetime import datetime
from datetime import timedelta

UPLOAD_FOLDER = 'static/Uploads/'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "thisisaencryptedmessage"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/subastas')
def subastas():
    if "user" in session:
        datosObras = SubirObras.select()
        return render_template('subastas.html', obras = datosObras)
    else:
        return redirect(url_for("login"))
    return render_template('subastas.html')

@app.route('/login', methods =["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["txtEmail"]
        password = request.form["txtPass"]
        validacion = RegistroUsuarios.selectWhere(user,password)
        if validacion!=-1:
            session["user"] = validacion[0]
        return redirect(url_for("homelog"))
    else:
        if "user" in session:
            return redirect(url_for("homelog"))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route('/signup')
def signup():
    datosCiudad = MantenedorCiudades.selectAll()
    return render_template('signup.html', cities = datosCiudad)

@app.route('/homeloged')
def homelog():
    if "user" in session:
        return render_template('homeloged.html')
    else:
        return redirect(url_for("login"))

@app.route('/aboutloged')
def aboutlog():
    if "user" in session:
        return render_template('aboudloged.html')
    else:
        return redirect(url_for("login"))

@app.route('/servicesloged')
def serviceslog():
    if "user" in session:
        return render_template('servicesloged.html')
    else:
        return redirect(url_for("login"))

@app.route('/piece')
def piece():
    datosEstilos = MantenedorEstilos.selectAll()
    if "user" in session:
        return render_template('addImg.html', styles = datosEstilos)
    else:
        return redirect(url_for("login"))

@app.route('/paises')
def country():
    if "user" in session:
        datosPais = MantenedorPaises.selectAll()
        return render_template('mantenedores/pais.html', countries = datosPais)
    else:
        return redirect(url_for("login"))

@app.route('/ciudad')
def city():
    if "user" in session:
        datosPais = MantenedorPaises.selectAll()
        datosCiudad = MantenedorCiudades.selectAll()
        return render_template('mantenedores/ciudad.html', countries = datosPais, cities = datosCiudad)
    else:
        return redirect(url_for("login"))

@app.route('/estilos')
def style():
    if "user" in session:
        datosEstilo = MantenedorEstilos.selectAll()
        return render_template('mantenedores/estilos.html', styles = datosEstilo)
    else:
        return redirect(url_for("login"))

@app.route('/admin')
def admin():
    if "user" in session:
        datosAdmin = MantenedorAdministradores.selectAll()
        return render_template('mantenedores/admin.html', admins = datosAdmin)
    else:
        return redirect(url_for("login"))

#Registrado
@app.route('/registered', methods=['POST'])
def registered():
    if "user" in session:
        return redirect(url_for("homelog"))
    else:
        if request.method == 'POST':            
            try:
                auxBtnRegistrar = request.form['btnRegistro']
                if auxBtnRegistrar == 'Registrarse':
                    print("XDDD")
                    email = request.form['txtEmail']
                    password = request.form['txtPass']
                    negocios = request.form['txtEmailNegocios']
                    nom = request.form['txtNombre']
                    apa = request.form['txtApa']
                    ama = request.form['txtAma']
                    nomArt = request.form['txtNomArt']
                    ciudad = request.form.get('txtCiudad')
                    fec = request.form['txtFec']                    
                    artista = Artistas.Artista(nom,apa,ama,nomArt,fec,negocios,ciudad,email,password)
                    RegistroUsuarios.insert(artista)
            except:
                pass
    return redirect(url_for("login"))

#Subir una obra
@app.route('/upload', methods=['POST'])
def upload():
    if "user" in session:
        if request.method == 'POST':
            try:
                auxBtn = request.form['btnAcept']
                if auxBtn == 'Subir':
                    image = request.files["imgObra"]
                    if image and allowed_file(image.filename):
                        imageName = secure_filename(image.filename)
                        username = session.get("user")
                        cod = str(username)+str(datetime.now())
                        nombre = request.form['txtNombre']
                        estilo = request.form.get('txtEstilo')
                        desc = request.form['txtDesc']
                        precio = int(request.form['txtPrecio'])
                        fechaSub = datetime.today() + timedelta(days=20)
                        auxObra = Obras.Obra(cod, nombre, desc, precio, fechaSub, estilo, username)
                        SubirObras.insert(auxObra, imageName)
                        image.save(os.path.join(app.config['UPLOAD_FOLDER'], imageName))
            except Exception as identifier:
                print(identifier)
    else:
        return redirect(url_for("login"))
    return redirect(url_for("piece"))

#Subastar
@app.route('/subastar/<string:id>', methods=['POST','GET'])
def auction(id):
    if "user" in session:
        if request.method == 'POST':
            try:
                auxBtn = request.form['btnAcept'+id]
                if auxBtn == 'Ofertar':
                    username = session.get("user")
                    puja = int(request.form['txtPuja'+id])
                    obra = request.form['txtObra'+id]
                    mejorPuja = int(request.form.get('txtMejor'+id))
                    pBase = int(request.form['txtBase'+id])
                    if mejorPuja<puja:
                        if pBase<puja:
                            subasta = Subastas.Subasta(obra, username, puja)
                            Subastar.insert(subasta)
                        else:
                            flash("No se puede ofertar un valor menor al precio base, lo sentimos.")
                            return redirect(url_for('subastas'))    
                    else:
                        flash("No se puede ofertar un valor menor a la puja más alta, lo sentimos.")
                        return redirect(url_for('subastas'))
            except Exception as identifier:
                print(identifier)
        return redirect(url_for('subastas'))
    else:
        return redirect(url_for("login"))

#Mantenedores 
#Mantenedor País
@app.route('/mantenedorPais', defaults={'id': None}, methods=['POST'])
@app.route('/mantenedorPais/<string:id>')
def MantenedorPais(id):
    if "user" in session:
        if request.method == 'POST':
            try:
                auxBtnInsert = request.form['btnAcept']
                if auxBtnInsert == 'Insertar':
                    auxCod = request.form['txtCod']
                    auxNom = request.form['txtNom']
                    auxPais = Paises.Pais(auxCod,auxNom)
                    MantenedorPaises.insert(auxPais)
                elif auxBtnInsert == 'Editar':
                    auxCod = request.form['txtCodEdit']
                    auxNom = request.form['txtNomEdit']
                    MantenedorPaises.update(auxCod,auxNom)
            except:
                print('Error')
        elif id:
            try:
                MantenedorPaises.deleteWhere(id)
            except:
                print("Error")
        return redirect(url_for('country'))
    else:
        return redirect(url_for("login"))

#Mantenedor Ciudad
@app.route('/mantenedorCiudad', defaults={'id': None}, methods=['POST'])
@app.route('/mantenedorCiudad/<string:id>')
def MantenedorCiudad(id):
    if "user" in session:
        if request.method == 'POST':
            try:
                auxBtnInsert = request.form['btnAcept']
                if auxBtnInsert == 'Insertar':
                    auxCod = request.form['txtCod']
                    auxNom = request.form['txtNom']
                    auxPais = request.form.get('txtPais')
                    auxCiudad = Ciudades.Ciudad(auxCod,auxNom,auxPais)
                    MantenedorCiudades.insert(auxCiudad)
                elif auxBtnInsert == "Editar":
                    auxCod = request.form['txtCodEdit']
                    auxNom = request.form['txtNomEdit']
                    print(auxCod+auxNom)
                    MantenedorCiudades.update(auxCod,auxNom)
            except:
                print('Error')
        elif id:
            try:
                MantenedorCiudades.deleteWhere(id)
            except:
                print("Error")
        return redirect(url_for('city'))
    else:
        return redirect(url_for("login"))

#Mantenedor Estilo
@app.route('/mantenedorEstilo', defaults={'id': None}, methods=['POST'])
@app.route('/mantenedorEstilo/<string:id>')
def mantenedorEstilo(id):
    if "user" in session:
        if request.method == 'POST':
            try:
                auxBtnInsert = request.form['btnAcept']
                if auxBtnInsert == 'Insertar':
                    auxCod = request.form['txtCod']
                    auxNom = request.form['txtNom']
                    auxEstilo = Estilos.Estilo(auxCod,auxNom)
                    MantenedorEstilos.insert(auxEstilo)
                elif auxBtnInsert == "Editar":
                    auxCod = request.form['txtCodEdit']
                    auxNom = request.form['txtNomEdit']
                    print(auxCod+auxNom)
                    MantenedorEstilos.update(auxCod,auxNom)
            except:
                print('Error')
        elif id:
            try:
                MantenedorEstilos.deleteWhere(id)
            except:
                print("Error")
        return redirect(url_for('style'))
    else:
        return redirect(url_for("login"))

#Mantenedor Admin
@app.route('/mantenedorAdmin', defaults={'id': None}, methods=['POST'])
@app.route('/mantenedorAdmin/<string:id>')
def mantenedorAdmin(id):
    if "user" in session:
        if request.method == 'POST':
            try:
                auxBtnInsert = request.form['btnAcept']
                if auxBtnInsert == 'Insertar':
                    nom = request.form['txtNom']
                    apa = request.form['txtApa']
                    ama = request.form['txtAma']
                    email = request.form['txtEmail']
                    password = request.form['txtPass']
                    adminis= Administradores.Administrador(0,nom,apa,ama,email,password)
                    MantenedorAdministradores.insert(adminis)
                elif auxBtnInsert == 'Editar':
                    cod = request.form['txtCodEdit']
                    nom = request.form['txtNomEdit']
                    apa = request.form['txtApaEdit']
                    ama = request.form['txtAmaEdit']
                    MantenedorAdministradores.update(cod,nom,apa,ama)
            except:
                print('Error')
        elif id:
            try:
                MantenedorAdministradores.deleteWhere(id)
            except:
                print("Error")
        return redirect(url_for('admin'))
    else:
        return redirect(url_for("login"))
        
if __name__ == '__main__':
    app.run(debug=True)