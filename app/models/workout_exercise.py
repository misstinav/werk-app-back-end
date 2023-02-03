# https://www.youtube.com/results?search_query=many+to+many+relationships+python

# https://www.rithmschool.com/courses/intermediate-flask/many-to-many-and-complex-associations

from app import db

class WorkoutExercises(db.Model):
  __tablename__ = "workout_exercise"
  workout_id = db.Column(db.Integer, db.ForeignKey('workout.workout_id'), primary_key=True, nullable=False)
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'), primary_key=True, nullable=False)

# WorkoutExercises = db.Table('workout_exercises',
#   db.Column('workout_id', db.Integer, db.ForeignKey('workout.workout_id')),
#   db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.exercise_id'))
# )


class Workout(db.Model):
  workout_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  workout_plan = db.Column(db.JSON, nullable=False)
  is_saved = db.Column(db.Boolean, nullable=True)
  exercises = db.relationship("Exercise", secondary="workout_exercise", backref='workouts')
  # trains = db.relationship("Exercise", secondary="workout_exercises", backref='practice')





class Exercise(db.Model):
  exercise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String, nullable=False)
  muscle = db.Column(db.String, nullable=False)
  equipment = db.Column(db.String, nullable=False)
  directions = db.Column(db.Text, nullable=False)


  #method where user puts in weight info per exercise
  # def log_exercise_weight(self):
  #   pass