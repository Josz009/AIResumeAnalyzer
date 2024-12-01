from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__)

# Load configurations from environment variables
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")
app.config["MONGO_URI"] = os.getenv("DATABASE_URL")

CORS(app, origins=["https://airesumeanalyzerfrontend.onrender.com"])

# Initialize MongoDB connection
mongo = PyMongo(app)

# Import routes
from app import routes
