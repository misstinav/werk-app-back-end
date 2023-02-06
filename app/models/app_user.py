from app import db

class AppUser(db.Model):
  appuser_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(20))
  password = db.Column(db.String)
  logged_exercise = db.Column(db.JSON)
  workouts = db.relationship("Workout", back_populates="app_user")