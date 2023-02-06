# import requests
# import os
# import json
# from flask import Blueprint, jsonify, make_response, abort, request
# from app.models.old_workout_exercise import Workout
# from app.models.old_user_workouts import AppUser
# from app.models.old_workout_exercise import Exercise
# from app.models.old_workout_exercise import WorkoutExercises

# from app.ol import db


# path = 'https://api.api-ninjas.com/v1/exercises'
# query_params = {
#   "type": "strength",
#   "muscle": "chest"
# }

# response = requests.get(path, params=query_params, headers={'X-Api-Key': EXERCISE_API_KEY})

# print("The value of the response is", response)
# print("The value of response.text, which contains a text description of the request, is", response.text)


# def validate_models(cls, model_id):
#   try:
#     model_id = int(model_id)
#   except:
#     abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

#   model = cls.query.get(model_id)

#   if not model:
#     abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
#   return model

################ USER ENDPOINTS ############################
# user_bp = Blueprint('user_bp', __name__, url_prefix="/users")

# @user_bp.route('/user', methods=["POST"])
# def create_user():
#   request_body = request.get_json()
#   new_user = AppUser(
#     username = request_body["username"],
#     ########### need to create way of securing password###########
#     password = request_body["password"]
#   )

#   db.session.add(new_user)
#   db.session.commit()

#   return make_response(jsonify(f"User {new_user.username} has been created"), 201)

# for testing purposes, comment out on final version
# @user_bp.route('/<user_id>', methods=["GET"])
# def get_user(user_id):
#   user = validate_models(AppUser, user_id)

#   return jsonify(user.workouts)
  
# @user_bp.route("/<user_id>/workouts", methods=["GET"])
# def get_all_user_workouts(user_id):
#   user = validate_models(AppUser, user_id)
#   workouts = Workout.query.all()

#   workouts_response = []
#   for workout in workouts:
#     if workout.user_id == user.user_id:
#       workouts_response.append(
#         {
#           "workout_id": workout.workout_id,
#           "workout_plan": workout.workout_plan
#         }
#       )
#   return jsonify(workouts_response)

# @user_bp.route('/<user_id>/workout', methods=["GET"])
# def get_workout(user_id):
  # user = validate_models(AppUser, user_id)
  # muscle_focus = request.args.get("focus")
  # exp_level = request.args.get("experience")
  # if not muscle_focus or not exp_level:
  #   return {"message": "must provide experience level and focus of workout"}

  # response = requests.get(
  #   "https://api.api-ninjas.com/v1/exercises",
  #   params={"type": "strength",
  #           "muscle": muscle_focus,
  #           "difficulty": exp_level},
  #   headers={'X-Api-Key': os.environ.get("EXERCISE_API_KEY")}
  # )


  # json_response = json.loads(response)
  # return json_response
  # workout_list = []
  # while len(workout_list) < 3:
  #   for item in response.json():
  #     workout_list.append(
  #       {
  #         'name' : item['name'],
  #         'muscle' : item['muscle'],
  #         'equipment': item['equipment'],
  #         'difficulty' : item['difficulty']
  #       }
  #     )
    # exercise = Exercise(
    #   name=item['name'],
    #   muscle=item['muscle'],
    #   equipment=item['equipment'],
    #   difficulty=item['difficulty']
    #   )
    
    # db.session.add(exercise)
    # db.session.commit()
    # workout_list.append(exercise)

  


  # workout = Workout(workout_plan=workout_list, is_saved=False)

  # db.session.add(workout)
  # db.session.commit()

  # user.workouts.append(workout)

  # db.session.commit()

  
  # return jsonify(workout_list)



  # db.session.add(workout)
  # user.workouts.append(workout.workout_id)
  # db.session.commit()





################ WORKOUT ENDPOINTS ############################
# workout_bp = Blueprint('workout_bp', __name__, url_prefix="/workouts")

# @workout_bp.route('/<user_id>/workouts', methods=["GET"])
# def get_all_user_workouts(user_id):
#   user = validate_models(User, user_id)
#   workouts = Workout.query.all()

#   workouts_response = []
#   for workout in workouts:
#     if workout.user_id == user.user_id:
#       workouts_response.append(
#         {
#           "workout_id": workout.workout_id,
#           "workout_plan": workout.workout_plan
#         }
#       )
#   return jsonify(workouts_response)

#this creates a new workout
























################ EXERCISE ENDPOINTS ############################




# @exercises_bp.route("", methods=["GET"])
# def read_all_exercises():
#   exercise_api_response = []

#   #how can we sort the data?

#   exercises = Exercise.query.all()

# #instead of adding directions below. Create a pop up that displays muscle, equipment, directions when an 'info' icon is selected
#   for exercise in exercises:
#     exercise_api_response.append({
#       "id": exercise.exercise_id,
#       "name": exercise.name
#       # "muscle": exercise.muscle,
#       # "equipment": exercise.equipment 
#     })
  
#   return jsonify(exercise_api_response)


# @exercises_bp.route("/<exercise_id>", methods=["GET"])
# def read_one_exercise(exercise_id):
#   exercise = validate_models(Exercise, exercise_id)

#   return{
#     "name": exercise.name,
#     "muscle": exercise.muscle,
#     "equipment": exercise.equipment,
#     "directions": exercise.directions
#   }


# @exercises_bp.route("/exercises", methods=["POST"])
# def create_exercise():
#   client_request_body = request.get_json()
#   new_exercise = Exercise(
#     name=client_request_body["name"],
#     muscle=client_request_body["muscle"],
#     equipment=client_request_body["equipment"],
#     directions=client_request_body["directions"]
#   )
#   db.session.add(new_exercise)
#   db.session.commit()

#   return make_response(jsonify(f"{new_exercise.name} has been created and added to your available exercises"), 201)


# @exercises_bp.route("/<exercise_id>", methods=["DELETE"])

# def delete_exercise(exercise_id):
#   exercise = validate_models(Exercise, exercise_id)

#   db.session.delete(exercise)
#   db.session.commit()

#   return make_response(jsonify("The exercise has been deleted"),200)