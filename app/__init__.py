from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
  app = Flask(__name__)

  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
  CORS(app)
  return app