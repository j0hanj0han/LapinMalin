# this part is for logging the jenkins status


import jenkins
import logging
import json

# Create and configure logger


logging.basicConfig(filename="./smartrabbit/jenkins_status.log",
                    format='%(asctime)s %(message)s')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)



# get all the jobs information in a dictionary
def get_jenkins_jobs():

    # configure your jenkins server here
    server = jenkins.Jenkins('http://localhost:8080', username='j0hanj0han', password='coconutz')
    user = server.get_whoami()
    version = server.get_version()
    # to check if the connection is okay
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
    jobs = server.get_jobs()
    logger.info(jobs)
    return jobs


get_jenkins_jobs()



