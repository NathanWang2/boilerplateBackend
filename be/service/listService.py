from bson import ObjectId  # For ObjectId to work
from bson.json_util import dumps, loads
from be.db import todoList
from be.model.todoTask import TodoTask

# TODO: Make a reqeuest to an outside json and do some parse testing.


def getTodoList():
    todo_cursor = todoList.find()  # probably need to wait for a res
    todo_list = list(todo_cursor)
    todo_json = dumps(todo_list)

    return todo_json


def addNewItem(req):

    # Check if the data is in a certain model that we have

    # If it is successful, then return 200 if not failed?
    # Look into forming a proper request?

    try:
        data = req.get_json()

        title = data["Title"]
        new_task = TodoTask(title)

        todoList.insert_one(new_task.getTaskObject())
        return "201"  # Realitically you'd want to send a response obj.
    except Exception as e:
        # Usually never want to do this, this is more for me to debug
        print("Error: ", e)
        return "401"


def removeSingleTask(taskId):

    try:
        del_response = todoList.delete_one({"_id": ObjectId(taskId)})

        if del_response.deleted_count == 1:
            return "204"
        else:
            return "404 Did not delete"
    except:
        return "404"
    pass
