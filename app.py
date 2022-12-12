from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def about():  # put application's code here
    #return 'Esta sección tendrá el acerca, sobre el prototipo en general'
    return render_template("./estudiante/acerca_de.html")
@app.route('/unidad1')
def get_unidad_uno():
    return "Enviará la unidad 1 al template"

@app.route('/unidad2')
def get_unidad_dos():
    return "Enviará la unidad 2 al template"

@app.route('/unidad3')
def get_unidad_tres():
    return "Enviará la unidad 3 al template"

@app.route('/unidad4')
def get_unidad_cuatro():
    return "Enviará la unidad 4 al template"

@app.route('/acerca-de')
def get_acerca():
    #return "Enviará info acerca del porque el prototipo"
    return render_template("./estudiante/acerca_de.html")

@app.route('/ingresar-datos')
def get_ingresar_datos():
    return "Mostrar una pantalla para ingresar los datos"

@app.route('/predecir')
def get_login():
    return "Envía el login, para iniciar sesión"



if __name__ == '__main__':
    app.run(debug=True)
