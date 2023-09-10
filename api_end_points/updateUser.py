from flask import Blueprint,request,jsonify

#for generating random strings that will act as id for the records
from bson.objectid import ObjectId

#hashing library
from werkzeug.security import generate_password_hash

updateUser=Blueprint('updateUser',__name__)

@updateUser.route('/users/<id>',methods=['PUT'])
def update_oneUser(id):
    from app import mongo

    _id=id
    user=request.json
    name=user['name']
    email=user['email']
    password=user['password']

    if name and email and password and request.method=='PUT':
        hashed_password=generate_password_hash(password)
        mongo.db.user_collection.update_one({'_id':ObjectId(id['$oid']) if '$oid' in  _id else ObjectId(id)},{'$set':{'name':name,'email':email,'password':hashed_password}})
        return jsonify('user details updated successfully')
    else:
        return jsonify("user can't be found to update values" )
