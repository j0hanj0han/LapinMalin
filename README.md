# LapinMalin
This is a Smart Rabbit Project

Summary : 
This project is a construction of 2 API in FLASK :  API server (FLASK REST+) and an API client (FLASK).
- The SERVER will check the status Jenkin's Job of an account (via login and password) and make the data available.
- The CLIENT request the API server to get the Jenkins Status.

The Rabbit is a lighting Robot has th same functions of the API Client : it will display the status of a Jenkin's job via a light (red for failed, green for success)

This project runs in an CI/CD environment integration : Jenkins/SonarQube  to get a better quality code. 
