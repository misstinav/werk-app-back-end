# https://www.youtube.com/results?search_query=many+to+many+relationships+python

from app import db

WorkoutExercises = db.Table('workout_exercises',
  # db.Column('id', db.Integer, primary_key=True),
  db.Column('workout_id', db.Integer, db.ForeignKey('workout.workout_id')),
  db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.exercise_id'))
)


class Workout(db.Model):
  workout_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  workout_plan = db.Column(db.JSON, nullable=False)
  training = db.relationship("Exercise", secondary="WorkoutExercises", backref='practice')


  #method where user puts in weight info per exercise
  def log_exercise_weight(self):
    pass



class Exercise(db.Model):
  exercise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String, nullable=False)
  muscle = db.Column(db.String)
  equipment = db.Column(db.String)
  directions = db.Column(db.Text)