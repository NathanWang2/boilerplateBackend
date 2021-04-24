from flask import Flask
from be.controller.listController import list_blueprint

app = Flask(__name__)
app.config['MONGO_DBNAME'] = "mongodb://localhost:27017"
app.config['MONGO_URI'] = 'TodoDB'

# This is where you want to add your new endpoints.
app.register_blueprint(list_blueprint)
