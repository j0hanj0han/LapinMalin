import requests
from flask import Flask, render_template

from API_CLIENT.config import SERVER_ADDRESS

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


@app.route('/settings', methods=['GET', 'POST'])
def get_settings():
        return render_template('settings.html')


#  launch the API here
if __name__ == '__main__':
    app.run(debug=True, port=4000)


