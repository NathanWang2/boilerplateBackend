from flask import Blueprint
from bson import ObjectId  # For ObjectId to work
from bson.json_util import dumps

list_blueprint = Blueprint("list_blueprint", __name__)


@list_blueprint.route("/", methods=["GET"])
def test():
    return "This is just a test, your backend is at least listening :)"


@list_blueprint.route("/list", methods=["GET"])
def getTodoList():

    todo_cursor = collection.find()
    todo_list = list(todo_cursor)
    todo_json = dumps(todo_list)

    return todo_json
