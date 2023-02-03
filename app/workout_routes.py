from flask import Blueprint, jsonify, make_response, abort, request
from app.models.workout_exercise import Workout
from app.models.user_workouts import User
from app import db
from app.exercise_routes import validate_models

workout_bp = Blueprint("workout_bp", __name__)


# @workout_bp.route("/", methods=["PUT"])

# def create_workout():
#   request_body = request.get_json()

#   # if "exp_level" not in request_body or "focus" not in request_body:
#   #   return {"details": "Please enter in your experience level and focus to get a workout"}, 400
  
#   new_workout = Workout(
#     workout_plan = {exercise_id : f"{exercise.name}"}
#   )


# def read_user_current_workout(user_id):
#   user = validate_models(User, user_id)
#   workout_plans = Workout.query.all()

#   workout_response = []
