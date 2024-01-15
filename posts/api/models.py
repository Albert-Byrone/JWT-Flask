from api import db


class Users(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(36), unique=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User {self.name}>"
