from app import db

class Exercise(db.Model):
  exercise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.Varchar, length=100)
  directions = db.Column(db.Text)

  