import requests
import json
from time import process_time


def test_FR1_1():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/register', json={
	"username" : "ghtdsss",
	"password" : "12356"	
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200


def test_FR1_2():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/register', json={
	"username" : "fffff",
	"password" : "123"	
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200


def test_FR1_3():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/register', json={
	"username" : "&%$!@&",
	"password" : "123"	
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200


def test_FR2_1():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/register', json={
	"username" : "fffff",
	"password" : "123"	
    })
    json_response = response.json()
    assert json_response['statuscode'] == 301

def test_FR2_2():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/register', json={
    "username" : "fffff",
    "password" : "123"  
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200

def test_FR3_1():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect', json={
    "username" : "wer",
    "password" : "123",
    "text1" : "www",
    "text2" : "www" 
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200
    assert json_response["similarity ratio"] == 100

def test_FR3_2():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect', json={
    "username" : "gggg",
    "password" : "123",
    "text1" : "www",
    "text2" : "www" 
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200
    assert json_response["similarity ratio"] == 100

def test_FR3_3():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect', json={
    "username" : "fffff",
    "password" : "123",
    "text1" : "www",
    "text2" : "www" 
    })
    json_response = response.json()
    assert json_response['statuscode'] == 303

def test_FR3_4():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect', json={
    "username" : "wer",
    "password" : "1234",
    "text1" : "www",
    "text2" : "www" 
    })
    json_response = response.json()
    assert json_response['statuscode'] == 302
    

def test_FR4_1():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/refill', json={
    "username" : "wsx",
    "admin_password" : "Admiral123",
    "refill_amt" : 10
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200
    assert json_response["tokens left"] == 226

def test_FR4_2():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/refill', json={
    "username" : "weesx",
    "admin_password" : "Admiral123",
    "refill_amt" : 10
    })
    json_response = response.json()
    assert json_response['statuscode'] == 301
    
def test_FR4_3():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/refill', json={
    "username" : "wsx",
    "admin_password" : "Admiral12345",
    "refill_amt" : 10
    })
    json_response = response.json()
    assert json_response['statuscode'] == 304

def test_FR4_4():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/refill', json={
    "username" : "wsx",
    "admin_password" : "Admiral123",
    "refill_amt" : 10
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200
    assert json_response["tokens left"] == 20

def test_NFR2_1():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/register', json={
    "username" : "wssdxwda",
    "password" : "123"  
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200

def test_NFR2_2():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect', json={
    "username" : "wer",
    "password" : "123",
    "text1" : "w",
    "text2" : "w" 
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200
    assert json_response["similarity ratio"] == 100

def test_NFR2_3():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/refill', json={
    "username" : "123",
    "admin_password" : "Admiral123",
    "refill_amt" : 5
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200
    assert json_response["tokens left"] == 31

def test_NFR3_1():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect', json={
    "username" : "wer",
    "password" : "123",
    "text1" : "我是谁",
    "text2" : "我是谁" 
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200
    assert json_response["similarity ratio"] == 100

def test_NFR3_2():
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect', json={
    "username" : "wer",
    "password" : "123",
    "text1" : "😀",
    "text2" : "😀" 
    })
    json_response = response.json()
    assert json_response['statuscode'] == 200
    assert json_response["similarity ratio"] == 100

def test_NFR4_1():
    t1_start = process_time()
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect', json={
    "username" : "wer",
    "password" : "123",
    "text1" : "www",
    "text2" : "www" 
    })
    json_response = response.json()
    t1_stop = process_time()
    Elapsed_time = t1_stop - t1_start
    assert Elapsed_time <= 0.1
    
def test_NFR4_2():
    t1_start = process_time()
    response = requests.post('http://ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect', json={
    "username" : "wer",
    "password" : "123",
    "text1" : "微服私访被u饿不饿不吃速测",
    "text2" : "金额发i俄服务i脑残粉i为访问"
    })
    json_response = response.json()
    t1_stop = process_time()
    Elapsed_time = t1_stop - t1_start
    assert Elapsed_time <= 0.1

