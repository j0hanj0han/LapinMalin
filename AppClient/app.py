import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def get_home():
    return render_template("home.html")


@app.route('/jobs')
def get_jobs():
    response = requests.get('http://127.0.0.1:5000/jobs')
    print(response.json())
    res = response.json()
    return render_template('jobs.html', res=res)



if __name__ == '__main__':
    app.run(debug=True, port=4000)
