from be.controller.listController import list_blueprint
from be import model, controller, service
from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017"
app.config['MONGO_DBNAME'] = 'TodoDB'

app.register_blueprint(list_blueprint)

mongo = PyMongo(app)
