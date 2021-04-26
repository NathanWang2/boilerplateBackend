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


def updateTask(req):
    # You could verify that it is the right _id/exists in the db.
    # For this I would need get_one for for that.

    updated_task = TodoTask()

    try:
        data = req.get_json()
        title = data['Title']
        _id = data["_id"]["$oid"]

        updated_task.setTitle(title)
        updated_task.setId(ObjectId(_id))

        # If you want to know, there are a lot of diff ways to handle updates.
        # You could either return false or write the doc yourself. etc.
        todoList.find_one_and_update({"_id": updated_task.getId()},
                                     {"$set":
                                      updated_task.getTaskObject()
                                      }, upsert=True)

        return "200"

    except Exception as e:
        print("Error: ", e)
        return "Fail 404"
