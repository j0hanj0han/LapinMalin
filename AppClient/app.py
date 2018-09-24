import requests
from flask import Flask, render_template

from AppClient.config import SERVER_ADDRESS, PORT

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def get_home():
    return render_template("home.html")


@app.route('/jobs')
def get_jobs():
    response = requests.get(SERVER_ADDRESS + '/jobs')
    res = response.json()
    return render_template('jobs.html', res=res)


#launch the API here
if __name__ == '__main__':
    app.run(debug=True, port=4000)
