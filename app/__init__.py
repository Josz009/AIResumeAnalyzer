from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Flask configurations
app.config["SECRET_KEY"] = "2ba00670e71b1938dca8df9b7ac91c28c694941a56d4bef8"
app.config["MONGO_URI"] = "mongodb+srv://jos_estrada87:Carlos09@healthandwelness.fxsekx1.mongodb.net/AIResumeBuilder?retryWrites=true&w=majority"

# Enable CORS
CORS(app, origins=[""https://airesumeanalyzer.onrender.com"])

# Initialize MongoDB connection
mongo = PyMongo(app)

# Import routes
from app import routes
