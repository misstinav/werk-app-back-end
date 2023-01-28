# https://www.youtube.com/results?search_query=many+to+many+relationships+python

from app import db

class Workout(db.Model):
  workout_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  training = db.relationship("Exercise", secondary="workouts_exercises", backref='practice')


  #method where user puts in weight info per exercise
  def log_exercise_weight(self):
    pass