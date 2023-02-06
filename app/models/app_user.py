from app import db

class AppUser(db.Model):
  __tablename__ = 'appuser'
  appuser_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(20))
  password = db.Column(db.String)
  logged_exercise = db.Column(db.JSON, nullable=True)
  workouts = db.relationship("Workout", back_populates="appuser")