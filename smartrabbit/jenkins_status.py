import pprint
from datetime import datetime

import jenkins


# get all the jobs information in a dictionary
def get_jenkins_jobs():
    # configure your jenkins server here
    server = jenkins.Jenkins('http://localhost:8080', username='j0hanj0han', password='coconutz')
    user = server.get_whoami()
    version = server.get_version()
    # to check if the connection is okay
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
    jobs = server.get_jobs()
    return jobs



