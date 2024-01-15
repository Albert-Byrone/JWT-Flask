from api import db


class User(db.Model):

  # __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  public_id = db.Column(db.Integer)
  name = db.Column(db.String(60))
  password = db.Column(db.String(60))