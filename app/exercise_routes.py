import requests
import os
from flask import Blueprint, jsonify, make_response, abort
from app.models.exercise import Exercise

# path = 'https://api.api-ninjas.com/v1/exercises'
# query_params = {
#   "type": "strength",
#   "muscle": "chest"
# }

# response = requests.get(path, params=query_params, headers={'X-Api-Key': EXERCISE_API_KEY})

# print("The value of the response is", response)
# print("The value of response.text, which contains a text description of the request, is", response.text)



exercises_bp = Blueprint("exercises_bp", __name__, url_prefix="/exercises")

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

@exercises_bp.route("", methods=["POST"])
def create_exercise():
  pass