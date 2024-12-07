from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hello_world():
    return '¡Hola de nuevo, Mundo!'

@app.route('/hola2')
def excel():
    return '¡Excel!'

@app.route('/Excel7')
def excel7():
    return '¡Excel7!'

@app.route('/hello_flask')  # Nueva ruta para la página principal
def hello_flask():
    return '¡Bienvenido a mi aplicación Flask!'

@app.route('/adios') # Nueva ruta para decir BYE
def goodbye():
    return '¡Hasta luego!'

if __name__ == '__main__':
    app.run(debug=True)


