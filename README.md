
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Jenkins](https://img.shields.io/jenkins/s/https/jenkins.qa.ubuntu.com/view/Precise/view/All%20Precise/job/precise-desktop-amd64_default.svg)](http://localhost:8080/job/SmartRabbit/)
![SonarQube](https://img.shields.io/badge/SonarQube-Quality%20Gate-brightgreen.svg)




# SMART SPOKY

:rabbit::rabbit::rabbit::rabbit::rabbit::rabbit::rabbit::rabbit::rabbit::rabbit::rabbit::rabbit::rabbit:

Summary : 
Spoky is a Lighting Robot which take a RGB color.
Actually Spoky calls his own API to get the color.
The aim of the project is to monitore Jenkin's Jobs of a team and make Spoky happy or not ('blue' if all jobs are in a success build or 'red' if any of build failed).


This project is a construction of 2 API in FLASK :  API server (FLASK REST+) and an API client (FLASK).
- The SERVER will check each Jenkin's Job status of an account  and put the Spoky Color to his own API (Spoky's API).
- The CLIENT request the API server to get the Jenkins Status.

This project runs in an CI/CD environment integration : Jenkins/SonarQube  to get a better quality code. 

## Installation 


`pip install -r requirements.txt`

jenkins-python package : a python wrapper for Jenkin's API.


## Quick Start


- config.py : address, login and password for the jenkins jobs you want to monitor
            and put the Spoky's ID you want to control.
            
- Get the SERVER started : launch app_server.py on the port 5000.

- Get the CLIENT started : launch app_client.py (in API Client folder)on port 4000 to check the status of Jenkins.