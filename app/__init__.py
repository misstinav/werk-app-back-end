from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
  app = Flask(__name__)

  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  if test_config is None:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
  else:
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

  #models imported for alembic setup
  from app.models.workout_exercise import WorkoutExercises
  from app.models.workout_exercise import Workout
  from app.models.workout_exercise import Exercise
  
  from app.models.user_workouts import UserWorkouts
  from app.models.user_workouts import User


  # from app.models.workouts_exercises import WorkoutExercises
  # from app.models.exercise import Exercise
  # from app.models.user import User
  # from app.models.workout import Workout
  # from app.models.user_workouts import UserWorkouts

  db.init_app(app)
  migrate.init_app(app, db)
  
  #register blueprints
  from .exercise_routes import exercises_bp
  app.register_blueprint(exercises_bp)

  from .workout_routes import workout_bp
  app.register_blueprint(workout_bp)

  CORS(app)
  return app