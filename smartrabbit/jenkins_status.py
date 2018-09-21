import pprint
from datetime import datetime

import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='j0hanj0han', password='coconutz')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

jobs = server.get_jobs(view_name='POEI')

for job in jobs:
    print(job['name'] +"    Status:" + job['color'])


jobs = server.get_jobs()
print(jobs)
last_build_number = server.get_job_info('Jenkins_Project_S1')
print(last_build_number)

# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'