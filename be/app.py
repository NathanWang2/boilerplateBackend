from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from controller.listController import list_blueprint

app = Flask(__name__)
app.register_blueprint(list_blueprint)

client = MongoClient("mongodb://localhost:27017")  # host uri
db = client.TodoDB  # Select the database
collection = db.todos  # Select the collection name
