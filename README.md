# Lambdatest-Assignment
## Assignmnet

We need a system where we provide a website link and want to capture the screenshot on chrome & Firefox in Ubuntu. Create a script which asks for a website link and spawns 2 containers parallely  and open that link in chrome  and Firefox, capture the screenshot, push them to s3 and provide 2 signed s3 links. Links should expire after 30 mins


## Solution

``` bash
# clone the repo
$ git https://github.com/vivekhz01/Lambdatest-Assignment.git

# go into directory
$ cd Lambdatest---Assignment

# change the config file
$ vim .aws/config

# add aws key credentials
$ vim .aws/credentials

# Install Docker and docker compose on local
Docker Link - https://docs.docker.com/engine/install/ubuntu/
Docker Compose link - https://docs.docker.com/compose/install/

# Install python and python-pip
apt install python
apt install python-pip

# Run the bash Script
$ sh start.sh https://google.com/

```
