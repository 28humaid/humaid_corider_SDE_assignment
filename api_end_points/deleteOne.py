from flask import Blueprint,jsonify
from flask_restful import Api,Resource
#for generating random strings that will act as id for the records
from bson.objectid import ObjectId

deleteOne=Blueprint('deleteOne',__name__)

api=Api(deleteOne)

class DeleteOne(Resource):
    def delete(self,id):
        from app import mongo
        if mongo.db.user_collection.find_one({'_id':ObjectId(id)}):
            mongo.db.user_collection.delete_one({'_id':ObjectId(id)})
            return jsonify("User deleted successfully !")
        else:
            return jsonify("User NOT found !")

api.add_resource(DeleteOne,'/users/<string:id>')