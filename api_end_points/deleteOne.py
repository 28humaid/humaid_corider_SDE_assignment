from flask import Blueprint,jsonify

#for generating random strings that will act as id for the records
from bson.objectid import ObjectId

deleteOne=Blueprint('deleteOne',__name__)

@deleteOne.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    from app import mongo

    if mongo.db.user_collection.find_one({'_id':ObjectId(id)}):
        mongo.db.user_collection.delete_one({'_id':ObjectId(id)})
        return jsonify("User deleted successfully !")
    else:
        return jsonify("User NOT found !")