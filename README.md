# 3XA3 Project
# Plagiarism Check

This is a webpage based project that uses pretrained Natural Language Procesing model called Spacy to compute pairwise similarity ratio between two documents. This allows user to register for the API using a unique username and password. With each registration, a user gets 6 free tokens. User calls the API giving his username, password and the two documents as string and gets back the similarity ratio. Each transcation costs the user 1 token and he has option to refill the tokens by paying for it. When Admin receives tghe pay, he call the API giving username, Admin password and the refill amount. The user now has sum of existing tokens and the refill amount. The API is hosted on AWS with host url "ec2-3-134-112-214.us-east-2.compute.amazonaws.com at port 800". You can also access the live webpage at "http://plagiarismcheck-com.stackstaging.com"

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### System Prerequisites

```
Python3
MongoDB
Docker
Docker-compose
Postman
Google Chrome
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
 Once the API is running, your backend is good to go. Go onto the webpage and  <br />
 * register using a username and password <br />
 * find the similarity ration by using your valid username, password and the two documents as string <br /> 
 * Refill tokens using your usename, admin password and refill amount as the inputs  <br />
 
 **Registration** <br />
<img width="1048" alt="Screen Shot 2020-04-06 at 11 27 42 PM" src="https://user-images.githubusercontent.com/41305591/78627346-3aaf1380-785f-11ea-920e-58d321d1049d.png"> <br />

 **Detecting similarity** <br />
 <img width="906" alt="Screen Shot 2020-04-06 at 11 28 41 PM" src="https://user-images.githubusercontent.com/41305591/78627414-5e725980-785f-11ea-97c0-cfaf057b30ca.png"> <br />

 Refilling tokens <br />
 <img width="896" alt="Screen Shot 2020-04-06 at 11 28 59 PM" src="https://user-images.githubusercontent.com/41305591/78627464-81047280-785f-11ea-95be-79b2d691f317.png">

 
 ## Running edge test cases ##
 Regsitering a user twice <br />
 <img width="758" alt="Screen Shot 2020-04-06 at 11 38 36 PM" src="https://user-images.githubusercontent.com/41305591/78627556-c0cb5a00-785f-11ea-8af1-7f00624c68b4.png">
 
 Invalid user name <br />
 <img width="766" alt="Screen Shot 2020-04-06 at 11 39 48 PM" src="https://user-images.githubusercontent.com/41305591/78627616-f07a6200-785f-11ea-920d-ab4e6e22a4b9.png">

 No more tokens <br />
 <img width="802" alt="Screen Shot 2020-04-06 at 11 42 07 PM" src="https://user-images.githubusercontent.com/41305591/78627743-3e8f6580-7860-11ea-9673-39cf868fb14b.png">

 
 Wrong Admin password <br />
 <img width="790" alt="Screen Shot 2020-04-06 at 11 42 55 PM" src="https://user-images.githubusercontent.com/41305591/78627792-5c5cca80-7860-11ea-837e-0028bec82ec0.png"> <br />
 

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

* Stack Overflow
* Udemy
* El Farouk Yaseer
