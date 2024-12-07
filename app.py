from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hello_world():
    return '¡Hola, Mundo! 2'

@app.route('/hola2')
def excel():
    return '¡Excel!'

@app.route('/Excel7')
def excel7():
    return '¡Excel7!'

if __name__ == '__main__':
    app.run(debug=True)

