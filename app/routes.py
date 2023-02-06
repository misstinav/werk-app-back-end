import requests
import os
import json
from flask import Blueprint, jsonify, make_response, abort, request
from app.models.workout_exercise import WorkoutExercise
from app.models.workout_exercise import Workout
from app.models.workout_exercise import Exercise
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



@exercises_bp.route("", methods=["GET"])
def get_exercises():
  # return {"message": "in the function"}
  exercises_response = []
  muscle_focus = request.args.get("focus")
  exp_level = request.args.get("experience")
  if not muscle_focus or not exp_level:
    return {"message": "must provide experience level and focus of workout"}

  response = requests.get(
    "https://api.api-ninjas.com/v1/exercises",
    params={"type": "strength",
            "muscle": muscle_focus,
            "difficulty": exp_level},
    headers={'X-Api-Key': os.environ.get("EXERCISE_API_KEY")}
  )

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
  
  for item in exercises_response:
    exercise = Exercise(
      name=item['name'],
      muscle=item['muscle'],
      equipment=item['equipment'],
      difficulty=item['difficulty']
    )
    db.session.add(exercise)
    db.session.commit()
  
  
  # return jsonify(exercises_response)




  
@exercises_bp.route("/<exercise_id>", methods=["GET"])
def get_one_exercise(exercise_id):
  exercise = validate_models(Exercise, exercise_id)

  return jsonify(exercise.to_dict())

# exercises_bp.route("/<user_id>/log_exercise", methods=["PATCH"])
# def log_exercise(exercise_id):
#   exercise = validate_models(Exercise, exercise_id)
  # sets = request.args.get("sets")
  # reps = request.args.get("reps")
  # weight = request.args.get("weight")