from app import db

class AppUser(db.Model):
  __tablename__ = 'appuser'
  appuser_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(20))
  password = db.Column(db.String)
  logged_exercise = db.Column(db.JSON, nullable=True)
  workouts = db.relationship("Workout", back_populates="appuser", lazy=True)

  def to_dict(self):
    appuser_as_dict = {}
    appuser_as_dict['user_id'] = self.appuser_id
    appuser_as_dict['logged_exercise'] = self.logged_exercise
    
    return appuser_as_dict