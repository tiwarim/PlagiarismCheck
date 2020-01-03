# Plagiarism Check

This is a Restful API that uses pretrained Natural Language Procesing model called Spacy to compute pairwise similarity ratio between two documents. This allows user to register for the API using a unique username and password. With each registration, a user gets 6 free tokens. User calls the API giving his username, password and the two documents as string and gets back the similarity ratio. Each transcation costs the user 1 token and he has option to refill the tokens by paying for it. When Admin receives tghe pay, he call the API giving username, Admin password and the refill amount. The user now has sum of existing tokens and the refill amount. The API is hosted on AWS with host url "ec2-18-224-246-224.us-east-2.compute.amazonaws.com:8000/"

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### System Prerequisites

```
Python3
MongoDB
Docker
Docker-compose
Postman
```
**Install Python requirements**
```
pip3 install -r requirements.txt
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Python : 
https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html 

Flask:
https://pypi.org/project/Flask/ 

MongoDB :
https://docs.mongodb.com/manual/installation/

Docker 
https://docs.docker.com/docker-for-mac/install/ 

Docker-compose 
https://docs.docker.com/compose/install/

Postman:
https://www.getpostman.com/downloads/ 
```

### Resource Chart Protocol

```
| Resource      |      URL      | Protocol   | Parameters                      | status codes
| ------------- | ------------- | ---------  | -------------                   | ------------- 
| Register      | /register     | POST       | username, password              | 200 OK, 301 user exists
| Detect        | /detect       | POST       | username, password, doc1, doc2  | 200 OK, 301 invalid user, 302 invalid password, 303 out of tokens
| Refill        | /refill       | POST       | username, password, refill amt  | 200 OK, 301 invalid user, 302 invalid password, 304 wrong Admin password

```



## Running the tests
"
In your local machine, go to your project directory and run
 * sudo docker-compose build <br />
 * sudo docker-compose up <br />
 Once the API is running, copy the host url and paste it in post man, and give your command after /. In postman, <br />
 * register using a username and password on a POST protocol with /register URL <br />
 * find the similarity ration by using your valid username, password and the two documents as string on a POST protocol with /detect URL<br /> 
 * Refill tokens using your usename, admin password and refill amount as the inputs to the api with POST protocol and /refill url <br />
 
 **Registration** <br />
<img width="480" height="350" alt="Screen Shot 2020-01-01 at 11 05 04 PM" src="https://user-images.githubusercontent.com/41305591/71651548-711f4480-2cec-11ea-8b75-f27702973a9a.png"> <br />
 **Detecting similarity** <br />
 <img width="410" eight="400" alt="Screen Shot 2020-01-01 at 11 13 09 PM" src="https://user-images.githubusercontent.com/41305591/71651682-85177600-2ced-11ea-8750-4031d3337db7.png"> <br />

 Refilling tokens <br />
 <img width="445" height="350" alt="Screen Shot 2020-01-01 at 11 24 57 PM" src="https://user-images.githubusercontent.com/41305591/71651745-fbb47380-2ced-11ea-8b60-6ca1d5d19b7d.png">
 
 ## Running edge test cases ##
 Regsitering a user twice <br />
 <img width="329" height="350" alt="Screen Shot 2020-01-01 at 8 37 38 PM" src="https://user-images.githubusercontent.com/41305591/71648762-97d28080-2cd6-11ea-9db0-66b25e1ed5d4.png"> <br />
 
 Invalid user name <br />
 <img width="342" alt="Screen Shot 2020-01-01 at 11 31 10 PM" src="https://user-images.githubusercontent.com/41305591/71651862-dc6a1600-2cee-11ea-8eef-99e223918987.png"><br />
 
 No more tokens <br />
 <img width="417" height="350" alt="Screen Shot 2020-01-01 at 11 28 59 PM" src="https://user-images.githubusercontent.com/41305591/71651814-90b76c80-2cee-11ea-8c8b-478304e167ca.png"><br />
 
 Wrong Admin password <br />
 <img width="359" alt="Screen Shot 2020-01-01 at 8 57 51 PM" src="https://user-images.githubusercontent.com/41305591/71649045-7030e780-2cd9-11ea-8edf-5bd7fd9f051c.png"> <br />
 
 


## Deployment

Create a EC2 instance in AWS console, download the pep file and run the following commands:  <br />
* ssh -i "Pem file location""pem file name".pem.txt "username"@"public dns of your instance"  <br />
 install docker and docker-compose.  <br />
* mkdir "directory name"  <br />
* cd "directory name"
* git clone "your git link to the application containing docker-compose.yml"  <br />
* sudo docker-compose build <br />
* sudo docker-compose up. <br />
 
 Your application should now be up and running on AWS
 
## Acknowledgments

* Udemy
* El Farouk Yaseer
