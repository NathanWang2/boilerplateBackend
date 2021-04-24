from flask import Blueprint
from be.service import listService

list_blueprint = Blueprint("list_blueprint", __name__)


@list_blueprint.route("/", methods=["GET"])
def test():
    return "This is just a test, your backend is at least listening :)"


@list_blueprint.route("/list", methods=["GET"])
def getTodoList():

    return listService.getTodoList()
