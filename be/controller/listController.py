from flask import Blueprint, request
from be.service import listService

list_blueprint = Blueprint("list_blueprint", __name__)


@list_blueprint.route("/", methods=["GET"])
def test():
    return "This is just a test, your backend is at least listening :)"


@list_blueprint.route("/list", methods=["GET"])
def getTodoList():

    return listService.getTodoList()


@list_blueprint.route("/addItem", methods=["POST"])
def addNewItem():
    return listService.addNewItem(request)


@list_blueprint.route("/removeTask/<taskId>", methods=["DELETE"])
def removeSingleTask(taskId):
    return listService.removeSingleTask(taskId)
