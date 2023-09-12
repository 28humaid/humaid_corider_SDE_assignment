from flask import Blueprint,request,jsonify
from flask_restful import Resource,Api
#for generating random strings that will act as id for the records
from bson.objectid import ObjectId

#hashing library
from werkzeug.security import generate_password_hash

updateUser=Blueprint('updateUser',__name__)

api=Api(updateUser)

class UpdateUser(Resource):
    def put(self,id):
        from app import mongo
        _id=id
        user=request.json
        name=user['name']
        email=user['email']
        password=user['password']

        if name and email and password and request.method=='PUT' and mongo.db.user_collection.find_one({'_id':ObjectId(id)}):
            hashed_password=generate_password_hash(password)
            mongo.db.user_collection.update_one({'_id':ObjectId(id['$oid']) if '$oid' in  _id else ObjectId(id)},{'$set':{'name':name,'email':email,'password':hashed_password}})
            return jsonify('User updated successfully')
        else:
            return jsonify('User cant be found to update values')


api.add_resource(UpdateUser,'/users/<string:id>')