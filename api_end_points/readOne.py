from flask import Blueprint

#importing bson library, in order to convert bson into json
from bson.json_util import dumps

#for generating random strings that will act as id for the records
from bson.objectid import ObjectId

readOne=Blueprint('readOne',__name__)
@readOne.route('/users/<id>', methods=['GET'])
def display_oneUser(id):
    from app import mongo
    user=mongo.db.user_collection.find_one({'_id':ObjectId(id)})
    resp=dumps(user)
    return resp