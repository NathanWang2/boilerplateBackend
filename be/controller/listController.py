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


@list_blueprint.route("/updateTask", methods=["PUT"])
def updateTask():
    # As a headsup, put might not work. If it doesn't, post is what you'll want
    # https://stackoverflow.com/questions/41868378/cant-use-put-method-with-flask
    # Good article about PUT vs PATCH https://medium.com/backticks-tildes/restful-api-design-put-vs-patch-4a061aa3ed0b

    # Another thing you could do is add the TaskID to the endpoint
    # Pass that in with the request data.
    return listService.updateTask(request)
