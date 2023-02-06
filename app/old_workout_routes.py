# from flask import Blueprint, jsonify, make_response, abort, request
# from app.models.old_workout_exercise import Workout
# from app.models.old_user_workouts import User
# from app.ol import db
# from app.old_exercise_routes import validate_models

# workout_bp = Blueprint("workout_bp", __name__)


# @workout_bp.route("/", methods=["PUT"])

# def create_workout():
#   request_body = request.get_json()

#   # if "exp_level" not in request_body or "focus" not in request_body:
#   #   return {"details": "Please enter in your experience level and focus to get a workout"}, 400
  
#   new_workout = Workout(
#     workout_plan = {exercise_id : f"{exercise.name}"}
#   )

