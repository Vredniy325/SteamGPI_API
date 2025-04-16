import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add the app directory to the path

from app.models import Game  # Importing models for migrations
# from app.models import User  # Commenting out the User import since it is not defined
