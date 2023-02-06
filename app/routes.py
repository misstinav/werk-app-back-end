import requests
import os
import json
from flask import Blueprint, jsonify, make_response, abort, request
from app.models.workout_exercise import WorkoutExercise
from app.models.workout_exercise import Workout
from app.models.workout_exercise import Exercise
from app.models.app_user import AppUser
from app import db


def validate_models(cls, model_id):
  try:
    model_id = int(model_id)
  except:
    abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

  model = cls.query.get(model_id)

  if not model:
    abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
  return model

############# EXERCISE ROUTES ####################
exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises")

# @exercises_bp.route("", methods=["GET"])
# def get_exercises():
#   # return {"message": "in the function"}
#   new_workout = Workout()
#   exercises_response = []
#   muscle_focus = request.args.get("focus")
#   exp_level = request.args.get("experience")
#   if not muscle_focus or not exp_level:
#     return {"message": "must provide experience level and focus of workout"}

#   response = requests.get(
#     "https://api.api-ninjas.com/v1/exercises",
#     params={"type": "strength",
#             "muscle": muscle_focus,
#             "difficulty": exp_level},
#     headers={'X-Api-Key': os.environ.get("EXERCISE_API_KEY")}
#   )

#   for item in response.json():
#     if len(exercises_response) < 6:
#       exercises_response.append(
#         {
#           'name' : item['name'],
#           'muscle' : item['muscle'],
#           'equipment' : item['equipment'],
#           'difficulty' : item['difficulty']
#         }
#       )
  
#   for item in exercises_response:
#     db.session.add(Exercise(
#       name=item['name'],
#       muscle=item['muscle'],
#       equipment=item['equipment'],
#       difficulty=item['difficulty']
#     ))
#     db.session.commit()
  
#   exercises = Exercise.query.all()

#   return jsonify(exercises)




  
@exercises_bp.route("/<exercise_id>", methods=["GET"])
def get_one_exercise(exercise_id):
  exercise = validate_models(Exercise, exercise_id)

  return jsonify(exercise.to_dict())

# appuser_bp.route("/<user_id>/log_exercise", methods=["PATCH"])
# def log_exercise(exercise_id):
#   exercise = validate_models(Exercise, exercise_id)
  # sets = request.args.get("sets")
  # reps = request.args.get("reps")
  # weight = request.args.get("weight")




# @exercises_bp.route("", methods=["POST"])
# def create_exercise():

#   request_body = request.get_json()
#   try:
#     new_exercise= Exercise(
#       name=request_body["name"],
#       muscle=request_body["muscle"],
#       difficulty=request_body["difficulty"]
#     )

#   except KeyError:
#     return {"details": "Missing Entry Description"}, 400
#   db.session.add(new_exercise)
#   db.session.commit()

#   return {
#     "id": new_exercise.exercise_id,
#     "name": new_exercise.name,
#     "muscle": new_exercise.muscle,
#     "difficulty": new_exercise.difficulty
#   }, 201



################# USER ENDPOINTS #######################
appuser_bp = Blueprint('appuser', __name__, url_prefix="/users")

@appuser_bp.route("", methods=["POST"])
def create_user():
  request_body = request.get_json()
  new_user = AppUser(
    username=request_body['username'],
    password=request_body['password']
  )
  db.session.add(new_user)
  db.session.commit()

  return jsonify(f"User {new_user.username} has been created")

### testing purposes, comment out for final version
@appuser_bp.route("", methods=["GET"])
def get_users():
  users = AppUser.query.all()

  users_response = []
  for user in users:
    users_response.append(
      {
        "id" : user.appuser_id,
        "username" : user.username
      }
    )
  
  return jsonify(users_response)


@appuser_bp.route("/<appuser_id>", methods=['GET'])
def get_single_user(appuser_id):
  user = validate_models(AppUser, appuser_id)

  return jsonify(user.username)

@appuser_bp.route("/<appuser_id>/workouts", methods=["GET"])
def get_all_user_workouts(appuser_id):
  user = validate_models(AppUser, appuser_id)
  workouts = Workout.query.all()

  workouts_response = []
  for workout in workouts:
    if workout.appuser_id == user.appuser_id:
      workouts_response.append(
        {
          "workout_id": workout.workout_id,
          "workout_plan": workout.workout_plan
        }
      )
  return jsonify(workouts_response)


@appuser_bp.route('/<appuser_id>/workout', methods=["GET"])
def get_workout(appuser_id):
  user = validate_models(AppUser, appuser_id)
  muscle_focus = request.args.get("muscle")
  exp_level = request.args.get("difficulty")
  if not muscle_focus:
    return {"message": "must provide experience level and focus of workout"}

  response = requests.get(
    "https://api.api-ninjas.com/v1/exercises",
    params={"type": "strength",
            "muscle": muscle_focus,
            "difficulty": exp_level},
    headers={'X-Api-Key': os.environ.get("EXERCISE_API_KEY")}
  )

  # json_response = json.loads(response)
  # return json_response
  workout_list = []
  exercises_response = []
  for item in response.json():
    if len(exercises_response) < 6:
      exercises_response.append(
        {
          'name' : item['name'],
          'muscle' : item['muscle'],
          'equipment' : item['equipment'],
          'difficulty' : item['difficulty']
        }
      )
  # return response.json()

  # if not exercises_response:
  #   return jsonify("Exercise response is empty")
  #   # exercise response is currently empty

  for item in exercises_response:
    new_exercise = Exercise(
      name=item['name'],
      muscle=item['muscle'],
      equipment=item['equipment'],
      difficulty=item['difficulty']
    )
    db.session.add(new_exercise)
    db.session.commit()
    workout_list.append(new_exercise.name)

  # # if not workout_list:
  # #   return {"message": "workout list is empty"}
  # #  # workout list is currently empty


  workout = Workout(workout_plan=workout_list, is_saved=False, appuser_id=user.appuser_id)

  db.session.add(workout)
  db.session.commit()

  
  return jsonify(f"{user.username} has a new workout with the following exercises: {workout_list}")