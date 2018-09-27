# this part is for logging the jenkins status
import json
import jenkins
import logging
from smartrabbit.Spoky_API import get_spoky_color, put_spoky_color, red, blue
from smartrabbit.config import JENKINS_ADDRESS, JENKINS_USERNAME, JENKINS_PASSWORD


# Put the jobs status in a log file
logging.basicConfig(filename="./jenkins_status.log",
                    format='[%(asctime)s]:'
                           ' %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Check Jenkins Job Status and Set Spoky Color (task in a loop in background)
def get_jenkins_jobs_loop():
    # configure your jenkins server here
    server = jenkins.Jenkins(JENKINS_ADDRESS, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)

    #  get all the jobs information
    jobs = server.get_jobs()
    logger.info(jobs)

    #  put the job status in a dictionary
    job_status = []
    for job in jobs:
        job_status.append(job['color'])
    print(job_status)

    #  send the put request to Spoky API to change the color
    if 'red' in job_status :
        print("Spoky not Happy : One ore more build failed :")
        for job in jobs:
            if job['color'] == "red":
                print("Fail for : " + job['name'])
                if get_spoky_color() != red:
                    put_spoky_color(red)
        print("The current color is : " + json.dumps(get_spoky_color()))

    else:
        print("Spoky Happy : all builds are success")
        if get_spoky_color() != blue:
            put_spoky_color(blue)
        print("The current color is :" + json.dumps(get_spoky_color()))

    print('---------------------------')
    return jobs

# Check Jenkins Job Status
def get_jenkins_jobs():
    server = jenkins.Jenkins(JENKINS_ADDRESS, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
    jobs = server.get_jobs()
    return jobs
