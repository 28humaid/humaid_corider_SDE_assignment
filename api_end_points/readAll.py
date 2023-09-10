from flask import Blueprint

#importing bson library, in order to convert bson into json
from bson.json_util import dumps

readAll=Blueprint('readAll',__name__)

@readAll.route('/users', methods=['GET'])
def display():
    from app import mongo
    users=mongo.db.user_collection.find()
    resp=dumps(users)
    return resp