from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hello_world():
    return '¡Hola de nuevo, Mundo!'

@app.route('/hola3')
def excel():
    return '¡Hola desde Excel!'

@app.route('/Excel7')
def excel7():
    return '¡Excel7!'

@app.route('/hello_flask')  # Nueva ruta para la página principal
def hello_flask():
    return '¡Bienvenido a mi aplicación Flask!'

@app.route('/adios') # Nueva ruta para decir BYE
def goodbye():
    return '¡Hasta luego!'

@app.route('/adios3') # Nueva ruta para decir BYE
def goodbye():
    return '¡Hasta luego3!'

@app.route('/adios4') # Nueva ruta para decir BYE
def goodbye():
    return '¡Hasta luego4!'

if __name__ == '__main__':
    app.run(debug=True)


