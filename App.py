from flask import Flask, render_template, request, flash, redirect, url_for
import Paises
import MantenedorPaises
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/homeloged')
def homelog():
    return render_template('homeloged.html')

@app.route('/aboutloged')
def aboutlog():
    return render_template('aboudloged.html')

@app.route('/servicesloged')
def serviceslog():
    return render_template('servicesloged.html')

@app.route('/piece')
def piece():
    return render_template('addImg.html')


@app.route('/paises')
def country():
    datos = MantenedorPaises.selectAll()
    return render_template('mantenedores/pais.html', countries = datos)

@app.route('/ciudad')
def city():
    return render_template('mantenedores/ciudad.html')

@app.route('/estilos')
def style():
    return render_template('mantenedores/estilos.html')

@app.route('/artistas')
def artist():
    return render_template('mantenedores/artistas.html')
#Mantenedores 

#Mantenedor País
@app.route('/mantenedorPais', defaults={'id': None}, methods=['POST'])
@app.route('/mantenedorPais/<string:id>')
def MantenedorPais(id):
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
                print(auxCod+auxNom)
                MantenedorPaises.update(auxCod,auxNom)
        except:
            print('Error')
    elif id:
        try:
            MantenedorPaises.deleteWhere(id)
        except:
            print("Error")
    return redirect(url_for('country'))

if __name__ == '__main__':
    app.run(debug=True)