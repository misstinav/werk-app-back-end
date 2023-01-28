from app import db

class WorkoutExercises(db.Model):
  __tablename__ = "workout_exercise"
  workout_id = db.Column(db.Integer, db.ForeignKey('workout.workout_id'), primary_key=True, nullable=False)
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'), primary_key=True, nullable=True)