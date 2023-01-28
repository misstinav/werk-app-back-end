from app import db

class User(db.Model):
  user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(20))
  workouts = db.relationship('Workout', secondary='user_workouts', backref='users')