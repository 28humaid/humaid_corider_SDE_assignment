from flask import Blueprint,jsonify
from flask_restful import Resource,Api
#importing bson library, in order to convert bson into json
from bson.json_util import dumps

#for generating random strings that will act as id for the records
from bson.objectid import ObjectId

readOne=Blueprint('readOne',__name__)
api=Api(readOne)

class ReadOne(Resource):
    def get(self,id):
        from app import mongo
        if mongo.db.user_collection.find_one({'_id':ObjectId(id)}):
            user=mongo.db.user_collection.find_one({'_id':ObjectId(id)})
            resp=dumps(user)
            return resp
        else:
            return jsonify('user NOT found')        

api.add_resource(ReadOne,'/users/<string:id>')
