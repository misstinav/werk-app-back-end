from app import db

class UserWorkouts(db.Model):
  __tablename__ = "user_workout"
  user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True, nullable=False)
  workout_id = db.Column(db.Integer, db.ForeignKey('workout.workout_id'), primary_key=True, nullable=False)