from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash
from api import db, app
from api.models  import Users
from flask_jwt_extended import create_access_token

import uuid


@app.route('/register', methods=['POST'])
def create_user():
  data = request.get_json()
  hashed_password = generate_password_hash(data['password'])

  new_user = Users(public_id=str(uuid.uuid4()), name=data['name'], password=data['password'], admin=False)
  db.session.add(new_user)
  db.session.commit()
  return jsonify({'success': True, "message": "User created successfully"})

# route that will allow all the registered users to log in.
# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# his route verifies the registered users in the Users table and provides the output in JSON format..
@app.route('/users', methods=['GET'])
def get_all_users(): 
 
   users = Users.query.all()
   result = []  
   for user in users:  
       user_data = {}  
       user_data['public_id'] = user.public_id 
       user_data['name'] = user.name
       user_data['password'] = user.password
       user_data['admin'] = user.admin
     
       result.append(user_data)  
   return jsonify({'users': result})
