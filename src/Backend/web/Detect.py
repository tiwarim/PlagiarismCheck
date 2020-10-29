# importing libraries
from sys_utils import *

# Resource Detect
"""
    Resource Detect takes input on a POST protocol and returns similarity ratio
    Parameters:
        namepassimg: contains username, password of the user and two string documents <JSON>
    Returns:
        retJson: contains status code and message <JSON>
"""
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
