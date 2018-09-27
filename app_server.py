import threading
import time
import requests
from flask import Flask
from flask_restplus import Api, Resource
from smartrabbit.jenkins_status import get_jenkins_jobs, get_jenkins_jobs_loop

app = Flask(__name__)
api = Api(app)

# Get Jenkins Status Jobs and Put Color For Spoky each 5 seconds
@app.before_first_request
def activate_job():
    def run_job():
        while True:
            get_jenkins_jobs_loop()
            time.sleep(5)

    thread = threading.Thread(target=run_job)
    thread.start()


# list of all jobs with their status : success or fail
@api.route('/jobs')
class Jobs(Resource):
    def get(self):
        return get_jenkins_jobs()

# details of a jenkins job
@api.route('/job/<int:job_id>')
class Job(Resource):
    def get(self, job_id):
        return {'job': get_jenkins_jobs()[job_id]}


def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            print('In start loop')
            try:
                r = requests.get('http://127.0.0.1:5000/')
                if r.status_code == 200:
                    print('Server started, quiting start_loop')
                    print('-------------------------------')
                    not_started = False
                print(r.status_code)
            except:
                print('Server not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()


if __name__ == '__main__':
    start_runner()
    app.run(debug=True, port=5000)


