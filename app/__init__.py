from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

  #models imported for alembic setup
  from app.models.app_user import AppUser
  from app. models.workout_exercise import WorkoutExercise
  from app. models.workout_exercise import Workout
  from app. models.workout_exercise import Exercise

  db.init_app(app)
  migrate.init_app(app, db)
  
  #register blueprints
  from .routes import exercises_bp
  app.register_blueprint(exercises_bp)

  from .routes import appuser_bp
  app.register_blueprint(appuser_bp)


  CORS(app)
  return app