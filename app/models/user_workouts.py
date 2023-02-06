# from app import db

# class UserWorkouts(db.Model):
#   __tablename__ = "user_workout"
#   user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True, nullable=False)
#   workout_id = db.Column(db.Integer, db.ForeignKey('workout.workout_id'), primary_key=True, nullable=False)

# UserWorkouts = db.Table('users_workouts',
#   db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
#   db.Column('workout_id', db.Integer, db.ForeignKey('workout.workout_id'))
# )


# class AppUser(db.Model):
#   appuser_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#   username = db.Column(db.String(20))
#   password = db.Column(db.String)
#   logged_exercise = db.Column(db.JSON)
#   workouts = db.relationship("Workout", back_populates="app_user")
#   workouts = db.relationship('Workout', secondary='users_workouts', backref='users')


