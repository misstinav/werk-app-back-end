import requests
import os
from flask import Blueprint, jsonify, make_response, abort, request
from app.models.workout_exercise import Exercise
from app import db


# path = 'https://api.api-ninjas.com/v1/exercises'
# query_params = {
#   "type": "strength",
#   "muscle": "chest"
# }

# response = requests.get(path, params=query_params, headers={'X-Api-Key': EXERCISE_API_KEY})

# print("The value of the response is", response)
# print("The value of response.text, which contains a text description of the request, is", response.text)



exercises_bp = Blueprint("exercises_bp", __name__, url_prefix="/exercises")

def verify_id_exists(exercise_id):
  try:
    type(exercise_id) == int
  except:
    make_response({"error message": f"{exercise_id} is not a valid search"}, 400)
  
  exercise = Exercise.query.get(exercise_id)
  if not exercise:
    make_response({"message": "id number not found"}, 404)

  return exercise

@exercises_bp.route("", methods=["GET"])
def read_all_exercises():
  exercise_api_response = []

  #how can we sort the data?

  exercises = Exercise.query.all()

#instead of adding directions below. Create a pop up that displays muscle, equipment, directions when an 'info' icon is selected
  for exercise in exercises:
    exercise_api_response.append({
      "id": exercise.exercise_id,
      "name": exercise.name
      # "muscle": exercise.muscle,
      # "equipment": exercise.equipment 
    })
  
  return jsonify(exercise_api_response)

@exercises_bp.route("/<exercise_id>", methods=["GET"])
def read_one_exercise(exercise_id):
  exercise = verify_id_exists(exercise_id)

  return{
    "name": exercise.name,
    "muscle": exercise.muscle,
    "equipment": exercise.equipment,
    "directions": exercise.directions
  }

@exercises_bp.route("", methods=["POST"])
def create_exercise():
  client_request_body = request.get_json()
  new_exercise = Exercise(
    name=client_request_body["name"],
    muscle=client_request_body["muscle"],
    equipment=client_request_body["equipment"],
    directions=client_request_body["directions"]
  )
  db.session.add(new_exercise)
  db.session.commit()

  return make_response(jsonify(f"{new_exercise.name} has been created and added to your available exercises"), 201)

@exercises_bp.route("/<exercise_id>", methods=["DELETE"])

def delete_exercise(exercise_id):
  exercise = verify_id_exists(exercise_id)

  db.session.delete(exercise)
  db.session.commit()

  return make_response(jsonify("The exercise has been deleted"),200)