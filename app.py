from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hello_world():
    return '¡Hola, Mundo! 2'

@app.route('/hola2')
def excel():
    return '¡Excel!'

if __name__ == '__main__':
    app.run(debug=True)


