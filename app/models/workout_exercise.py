# https://www.youtube.com/results?search_query=many+to+many+relationships+python

# https://www.rithmschool.com/courses/intermediate-flask/many-to-many-and-complex-associations

from app import db
from datetime import date

class WorkoutExercise(db.Model):
  __tablename__ = "workout_exercise"
  workout_id = db.Column(db.Integer, db.ForeignKey('workout.workout_id'), primary_key=True, nullable=False)
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'), primary_key=True, nullable=False)

# WorkoutExercises = db.Table('workout_exercises',
#   db.Column('workout_id', db.Integer, db.ForeignKey('workout.workout_id')),
#   db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.exercise_id'))
# )

class Workout(db.Model):
  __tablename__ = 'workout'
  workout_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  workout_plan = db.Column(db.JSON, nullable=False)
  is_saved = db.Column(db.Boolean, nullable=True)
  appuser_id = db.Column(db.Integer, db.ForeignKey("appuser.appuser_id"))
  appuser = db.relationship("AppUser", back_populates="workouts")
  exercises = db.relationship("Exercise", secondary="workout_exercise", backref='workouts')
  # trains = db.relationship("Exercise", secondary="workout_exercises", backref='practice')

class Exercise(db.Model):
  __tablename__ = 'exercise'
  exercise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String, nullable=False)
  muscle = db.Column(db.String, nullable=False)
  equipment = db.Column(db.String, nullable=False)
  difficulty = db.Column(db.String, nullable=False)
  completed_at = db.Column(db.Date, nullable=True)

  def to_dict(self):
    exercise_as_dict = {}
    exercise_as_dict['name'] = self.name
    exercise_as_dict['muscle'] = self.muscle
    exercise_as_dict['equipment'] = self.equipment
    exercise_as_dict['difficulty'] = self.difficulty
    
    return exercise_as_dict

  def mark_completed(self):
    self.completed_at = date.today()


#   #method where user puts in weight info per exercise
#   # def log_exercise_weight(self):
#   #   pass