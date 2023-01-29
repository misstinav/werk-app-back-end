from app import db

class Exercise(db.Model):
  exercise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String, nullable=False)
  muscle = db.Column(db.String)
  equipment = db.Column(db.String)
  directions = db.Column(db.Text)
