from flask import Flask
from flask_restplus import Api, Resource

from smartrabbit.jenkins_status import jobs

app = Flask(__name__)
api = Api(app)


@api.route('/jobs')
class Jobs(Resource):
    def get(self):
        return jobs

@api.route('/job/<int:job_id>')
class Job(Resource):
    def get(self, job_id):
        return {'job': jobs[job_id]}


if __name__ == '__main__':
    app.run(debug=True)
