from flask import Flask
from waitress import serve


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    #app.debug = True
    app.run(port=8080)
    app.run()
    #serve(app, host='127.0.0.1', port=80)
