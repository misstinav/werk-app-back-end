from flask import Blueprint, jsonify, make_response, abort, request
from app.models.workout_exercise import Workout
from app import db

workout_bp = Blueprint("workout_bp", __name__, url_prefix="/workouts")

