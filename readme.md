# JIRA version automation tool
Support for the following:
* Creating a version.
* Adding issues to version.
* Transitioning issues.
Add
Dockerized automation tool so that no dependency installation is required from consuming machine.

## Build image
``` 
docker build -t jira-automation .
```
Note: first build will take longer than usual because python will have to be pulled from docker hub.
Each time a change is made to src code.
Rebuild the image with the command above.

## Run image as container
``` 
docker run jira-automation
```
This will run the script within the docker container.

