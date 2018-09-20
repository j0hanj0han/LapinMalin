from flask import Flask

from Subfolder.test2 import habib

app = Flask(__name__)

def test():
    return habib

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return 'Hello Test!'

azerty
if __name__ == '__main__':
    app.run()


johan = "developper"