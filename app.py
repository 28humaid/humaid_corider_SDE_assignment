#import the flask library
from flask import Flask

#python library to interact with MongoDB
from flask_pymongo import PyMongo

from flask_restful import fields

from api_end_points.readAll import readAll
from api_end_points.createUser import createUser
from api_end_points.readOne import readOne
from api_end_points.deleteOne import deleteOne
from api_end_points.updateUser import updateUser

app=Flask(__name__)

app.secret_key="secretkey"

#connecting database
app.config['MONGO_URI']="mongodb://localhost:27017/user_db"
mongo=PyMongo(app)

resource_fields ={
    'id':fields.String,
    'name':fields.String,
    'email':fields.String,
    'password':fields.String
}

#Creates a new user with the specified data.
app.register_blueprint(createUser)

#Returns a list of all users
app.register_blueprint(readAll)

#Returns the user with the specified ID
app.register_blueprint(readOne)

# Deletes the user with the specified ID
app.register_blueprint(deleteOne)

# Updates the user with the specified ID with the new data.
app.register_blueprint(updateUser)

#to run the app
if __name__=="__main__":
    app.run(debug=True)