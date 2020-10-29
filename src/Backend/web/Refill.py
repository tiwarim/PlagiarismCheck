# importing libraries
from sys_utils import *

# Resource refill
"""
    Resource Refill takes input on a POST protocol and adds to the existing tokens 
    Parameters:
        namepassref: contains username, admin password and refill amount <JSON>
    Returns:
        retJson: contains status code and message <JSON>
"""
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
