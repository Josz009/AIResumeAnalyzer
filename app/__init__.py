from flask import Flask
from flask_pymongo import PyMongo
import os

# Initialize Flask app
app = Flask(__name__)

# Load configurations from environment variables
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")
app.config["MONGO_URI"] = os.getenv("DATABASE_URL")

# Initialize MongoDB connection
mongo = PyMongo(app)

# Import routes
from app import routes
