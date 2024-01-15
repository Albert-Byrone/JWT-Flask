from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash
from api import db, app
from api.models  import User
import uuid


@app.route('/register', methods=['POST'])
def create_user():
  data = request.get_json()
  hashed_password = generate_password_hash(data['password'])

  new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=data['password'])
  db.session.add(new_user)
  db.session.commit()
  return jsonify({'success': True, "message": "User created successfully"})
