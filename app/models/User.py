from app import db

class User(db.Model):
  user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(20))
  password = db.Column(db.String)
  workouts = db.relationship('Workout', secondary='user_workouts', backref='users')