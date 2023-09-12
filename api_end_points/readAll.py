from flask import Blueprint
from flask_restful import Resource, Api
#importing bson library, in order to convert bson into json
from bson.json_util import dumps

readAll=Blueprint('readAll',__name__)
api=Api(readAll)

class ReadAllUsers(Resource):
    def get(self):
        from app import mongo
        users=mongo.db.user_collection.find()
        resp=dumps(users)
        return resp

api.add_resource(ReadAllUsers,'/users')