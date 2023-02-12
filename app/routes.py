import requests
import os
import json
import random
from datetime import date, datetime
from sqlalchemy import and_
from flask import Blueprint, jsonify, make_response, abort, request
from app.models.workout_exercise import WorkoutExercise
from app.models.workout_exercise import Workout
from app.models.workout_exercise import Exercise
from app.models.app_user import AppUser
from app import db


# sqlalchemy querying common operators
# https://rimsovankiry.medium.com/sqlalchemy-query-with-common-filters-c7adbd3321a6


def validate_models(cls, model_id):
  try:
    model_id = int(model_id)
  except:
    abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

  model = cls.query.get(model_id)

  if not model:
    abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
  return model


################# USER ENDPOINTS #######################
appuser_bp = Blueprint('appuser', __name__, url_prefix="/users")

@appuser_bp.route("", methods=["POST"])
def create_user():
  request_body = request.get_json()
  if not request_body['username'] or not request_body['password']:
    return "Please enter a username and password to create an account"
  else:
    new_user = AppUser(
      username=request_body['username'],
      password=request_body['password']
    )
    db.session.add(new_user)
    db.session.commit()

  return jsonify(f"User {new_user.username} has been created")


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
  
  return {
    "id" : user.appuser_id,
    "username" : user.username,
    "logged_exercises" : user.logged_exercise
  }

  return jsonify(response)


########### USER WORKOUT ENDPOINTS ############
@appuser_bp.route("/<appuser_id>/workouts", methods=["GET"])
def get_all_user_workouts(appuser_id):
  user = validate_models(AppUser, appuser_id)
  workouts = Workout.query.filter(Workout.appuser_id == user.appuser_id)
  # could be useful later. Can delete if not used at all
  # workout_id_list = [workout.workout_id for workout in workouts]
  
  workouts_dict_list = []
  for workout in workouts:
    exercise_name_list = []
    workout_exercise = WorkoutExercise.query.filter_by(workout_id=workout.workout_id)
    for item in workout_exercise:
      exercise = validate_models(Exercise, item.exercise_id)
      exercise_name_list.append(exercise.name)
    if not exercise_name_list:
      continue
    workouts_dict_list.append({
      f"workout{workout.workout_id}" : exercise_name_list
    })

  return workouts_dict_list


@appuser_bp.route("/<appuser_id>/workouts", methods=["POST"])
def create_workout(appuser_id):
  user = validate_models(AppUser, appuser_id)
  request_body = request.get_json()
  muscle_focus = request_body[1]
  exp_level = request_body[0]

  if not muscle_focus or not exp_level:
    return {"message": "must provide experience level and focus of workout"}

  if exp_level == 'beginner':
    exercises = Exercise.query.filter(
      and_(Exercise.muscle == muscle_focus, Exercise.difficulty == exp_level))
  else:
    exercises = Exercise.query.filter(Exercise.muscle == muscle_focus)

  # cant randomize object query. figure it out
  # exercise = random.choice(exercises)

  new_workout = Workout(appuser_id=user.appuser_id)
  db.session.add(new_workout)
  db.session.commit()

  workout_list = []
  for exercise in exercises:
    print(exercise)
    if len(workout_list) < 6:
      if exercise.name not in workout_list:
        workout_list.append(exercise.name)
        new_workout.exercises.append(exercise)
        db.session.commit()
    else:
      break
  print(workout_list)
  # return jsonify(f"{user.username} has a new workout with the following exercises: {workout_list}")
  return jsonify(workout_list)


####SOSOSOSOSOSOSOSOSOSOSOSOSOSOSOSOSOSOSOSOSOSOSOSOS##
@appuser_bp.route("/<appuser_id>/workouts/<workout_id>/log_exercise", methods=["PATCH"])
def patch_logged_exercise(appuser_id, workout_id):
  user = validate_models(AppUser, appuser_id)
  workout = validate_models(Workout, workout_id)
  workout_exercise = WorkoutExercise.query.filter(WorkoutExercise.workout_id == workout.workout_id)
  today = date.today().isoformat()
  
  exercise_ids_list = []
  for item in workout_exercise:
    exercise_ids_list.append(item.exercise_id)
  # return exercise_ids_list
  temp = [user.logged_exercise]

  user.logged_exercise = {}
  db.session.commit()

  exercise_name = request.args.get("exercise name")
  exercise_id = request.args.get("exercise id")
  if not exercise_name:
    return "Please enter an exercise name"

  log_exercise(user.appuser_id, exercise_id)
  if exercise_name not in temp:
    temp.append({
      f"{exercise_name}" : [today]
    })
  else:
    temp[f"{exercise_name}"].append(today)

  user.logged_exercise = temp
  db.session.commit()

  return {
    "username" : user.username,
    "logged exercise": user.logged_exercise
  }

# @appuser_bp.route("/<appuser_id>/exercises/<exercise_id>/completed_at", methods=["PATCH"])
def log_exercise(appuser_id, exercise_id):
  user = validate_models(AppUser, appuser_id)
  exercise = validate_models(Exercise, exercise_id)
  reps = int(request.args.get("reps"))
  weight = int(request.args.get("weight"))
  
  if not reps or not weight:
    return "Please enter your reps and weight in lb to save set"

  # save off the current completed_at JSON in temp
  temp = exercise.completed_at

  # Clear out of db exercise.completed at
  exercise.completed_at = {}
  db.session.commit()
  
  # Modify temp
  completed_at_list = []

  if user.username not in temp:
    temp.append({
      user.username : []
    })

  today = date.today().isoformat()
  if temp[user.username]:
    temp[user.username].append({
      today : [
        {"reps" :[reps]},
        {"weight" : [weight]}
      ]
    })
  else:
    temp[user.username] = [
      {
        today : [
          {"reps" :[reps]},
          {"weight" : [weight]}
        ]
      }
    ]
# # # # # # # # # Coming back to code  L A T E R # # # # # # # # # # # 
      ### if username present in temp. Then compare date object in username to today's date to add more than 1 set per day ###
    # for date_obj in temp[user.username]:
      # temp = str(date_obj)
      # dt_tuple = tuple([int(x) for x in temp[2:1].split('-')])
      # temp_date = datetime.datetime.strptime(dt_tuple, '%Y-%m-%d')
      # today = datetime.strptime(today, '%Y-%m-%d')
      # if temp_date == today:
      #   return "we okay"
      # if date_obj == today:
      #   # return "inside"
      #   for set_data in date_obj:
      #     set_data['reps'].append(reps)
      #     set_data['weight'].append(weight)


  # Saving this as temp works because it was empty
  exercise.completed_at = temp
  db.session.commit()



  # completed_at_list = []
  # for user_obj in exercise.completed_at:
  #   if user_obj == user.username:
  #     for date_obj in user_obj:
  #       if date_obj == today.isoformat():
  #         completed_at_list.append({date_obj})
  # return f"Here's the obj{completed_at_list}"
  # return temp

  return "Set has been logged"




@appuser_bp.route("<appuser_id>/workouts/<workout_id>/save", methods=["PATCH"])
def save_unsaved_workout(appuser_id, workout_id):
  user = validate_models(AppUser, appuser_id)
  workout = validate_models(Workout, workout_id)
  if workout.appuser_id == user.appuser_id:
    workout.save_workout()
    db.session.commit()
  else:
    return f"{user.username} does not have access to that workout"

  return "Workout has been saved"


@appuser_bp.route("<appuser_id>/workouts/<workout_id>/unsave", methods=["PATCH"])
def unsave_saved_workout(appuser_id, workout_id):
  user = validate_models(AppUser, appuser_id)
  workout = validate_models(Workout, workout_id)
  if workout.appuser_id == user.appuser_id:
    workout.unsave_workout()
    db.session.commit()
  else:
    return f"{user.username} does not have that workout saved"

  return "Workout has been removed from the saved list"













############# EXERCISE ROUTES ####################
exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises")

# @exercises_bp.route("", methods=["POST"])
# def create_all_exercises():
#   response = requests.get(
#   "https://api.api-ninjas.com/v1/exercises",
#   params={"type": "strength",
#           "muscle": "abdominals",
#           "difficulty": "intermediate"},
#   headers={'X-Api-Key': os.environ.get("EXERCISE_API_KEY")}
#   )
#   exercises_response = []
#   for item in response.json():
#     exercises_response.append(
#       {
#         'name' : item['name'],
#         'muscle' : item['muscle'],
#         'equipment' : item['equipment'],
#         'difficulty' : item['difficulty']
#       }
#     )
#   for item in exercises_response:
#     new_exercise = Exercise(
#       name=item['name'],
#       muscle=item['muscle'],
#       equipment=item['equipment'],
#       difficulty=item['difficulty']
#     )
#     db.session.add(new_exercise)
#     db.session.commit()

#   return "Exercises have been added to the database"



@exercises_bp.route("", methods=["GET"])
def get_all_exercises():
  exercises = Exercise.query.all()
  
  exercises_response = []
  for exercise in exercises:
    exercises_response.append(
      exercise.to_dict()
    )
  return exercises_response

@exercises_bp.route("/<exercise_id>", methods=["GET"])
def get_one_exercise(exercise_id):
  exercise = validate_models(Exercise, exercise_id)

  return jsonify(exercise.to_dict())
