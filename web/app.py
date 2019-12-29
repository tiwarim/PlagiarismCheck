# import libraries

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt # for hashing the password
import spacy # for predicting the similarity

app = Flask(__name__)
api = Api(app) # initialize that this app would be an api

client = MongoClient("mongodb://db:27017") # connecting mkongodb to our database db at the default port

db = client.SimilarityDB
users = db["users"] # our collection users


def userExists(username):
    if users.find({"username": username}).count() == 0:
        return False
    else:
        return True

# Resource Register
class Register(Resource):
    def post(self):
        namepass = request.get_json()
        username = namepass["username"]
        password = namepass["password"]

        # check if the user already exists
        if userExists(username):
            retJson = {
                "statuscode" : 301,
                "message" : "User Already exists"
            }
            return jsonify(retJson)

        hashedpw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert({
            "username" : username,
            "password" : hashedpw,
            "tokens" : 6
        })
        retJson = {
            "statuscode" : 200,
            "message" : "you successfuly signed up for the api"
        }
        return jsonify(retJson)


def verifypw(username, password):
    hashed_pw = users.find({
        "username" : username
    })[0]["password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def countTokens(username):
    num_tokens = users.find({
        "username" : username
    })[0]["tokens"]
    return num_tokens

# Resource Detect
class Detect(Resource):
    def post(self):
        namepasstext = request.get_json()
        username = namepasstext["username"]
        password = namepasstext["password"]
        text1 = namepasstext["text1"]
        text2 = namepasstext["text2"]

        if not userExists(username):
            retJson = {
                "statuscode" : 301,
                "message" : "User does not exit"
            }
            return jsonify(retJson)
        
        correct_pw = verifypw(username, password)
        if not correct_pw:
            retJson = {
                "statuscode" : 302,
                "message" : "Invalid password"
            }
            return jsonify(retJson)

        num_tokens = countTokens(username)
        if num_tokens <= 0 :
            retJson = {
                "statuscode" : 303,
                "message" : "Out of tokens, please refill"
            }
            return jsonify(retJson)

        # calculate edit distance. We use the pretained spacy model to predict the similarity of two strings goven to us
        nlp = spacy.load('en_core_web_sm') # loaded the spacy model
        
        text1 = nlp(text1)  # change from string to natural language processing model sentence
        text2 = nlp(text2)

        # ratio of similarity between 0 and 1 for the text1 and text2. closer the one, more the similarity
        # 0 = text1 and text2 are very different and 1 = text1 and text2 are almost or entirely similar

        ratio = text1.similarity(text2)
        
        retJson = {
            "statuscode" : 200,
            "message" : "Similarity ration calculated",
            "similarity ratio" : ratio
        }

        users.update({
            "username":username,
        },
        {
            "$set": {
                "tokens" : num_tokens -1
            }
        }
        )
        return jsonify(retJson)


# Resource refill
class Refill(Resource):
    def post(self):
        namepassref = request.get_json()
        username = namepassref["username"]
        admin_password = namepassref["admin_password"]
        refill_amt = namepassref["refill_amt"]

        if not userExists(username):
            retJson = {
                "statuscode" : 301,
                "message" : "User does not exit"
            }
            return jsonify(retJson)
        
        correct_admin_password = "Admiral123"

        if not correct_admin_password == admin_password:
            retJson = {
                "statuscode" : 304,
                "message" : "Invalid admin password"
            }
            return jsonify(retJson)

        num_tokens = countTokens(username)

        users.update({
            "username":username,
        },
        {
            "$set": {
                "tokens" : num_tokens + refill_amt
            }
        }
        )

        retJson = {
            "statuscode" : 200,
            "message" : "Tokens refilled successfully"
        }
        return jsonify(retJson)

api.add_resource(Register, "/register")
api.add_resource(Detect, "/detect")
api.add_resource(Refill, "/refill")

if __name__ == "__main__":
    app.run(host="0.0.0.0")



