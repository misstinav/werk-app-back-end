import pytest

from app import create_app
from app import db

# from app.models.exercise import Exercise
from app.models.workout_exercise import Workout
from app.models.user import User


@pytest.fixture
def app():
  app = create_app({"TESTING": True})

  with app.app_context():
    db.create_all()
    yield app

  with app.app_context():
    db.drop_all()
  


@pytest.fixture
def client(app):
  return app.test_client()

@pytest.fixture
def one_exercise(app):
  new_exercise = Exercise(
    name="Barbell glute bridge",
    muscle="glutes",
    equipment="barbell",
    instructions="Begin seated on the ground with a loaded barbell over your legs. Using a fat bar or having a pad on the bar can greatly reduce the discomfort caused by this exercise. Roll the bar so that it is directly above your hips, and lay down flat on the floor. Begin the movement by driving through with your heels, extending your hips vertically through the bar. Your weight should be supported by your upper back and the heels of your feet. Extend as far as possible, then reverse the motion to return to the starting position.")
  db.session.add(new_exercise)
  db.session.commit()
  