from flask import Flask
from flask_restplus import Api, Resource

from smartrabbit.jenkins_status import get_jenkins_jobs

app = Flask(__name__)
api = Api(app)


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


if __name__ == '__main__':
    app.run(debug=True)
