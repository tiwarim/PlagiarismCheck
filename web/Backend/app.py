# importing libraries
from utils import *

app = Flask(__name__)
api = Api(app) # initialize that this app would be an api

# assigning a route to the resources 
api.add_resource(Register, "/register")
api.add_resource(Detect, "/detect")
api.add_resource(Refill, "/refill")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8000)



