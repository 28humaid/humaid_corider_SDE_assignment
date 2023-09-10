from flask import Blueprint,jsonify, request

#hashing library
from werkzeug.security import generate_password_hash
createUser=Blueprint('createUser',__name__)

@createUser.route('/users', methods=['POST'])
def add_user():

    from app import mongo
    
    user=request.json
    name=user['name']
    email=user['email']
    password=user['password']

    if name and email and password and request.method=='POST':
        hashed_password=generate_password_hash(password)
        id=mongo.db.user_collection.insert_one({'name':name,'email':email,'password':hashed_password})
        return jsonify("User added successfully")
    else:
        return jsonify("User can't be added")