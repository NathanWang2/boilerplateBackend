from bson import ObjectId  # For ObjectId to work
from bson.json_util import dumps
from be.db import todoList


def getTodoList():
    todo_cursor = todoList.find()
    todo_list = list(todo_cursor)
    todo_json = dumps(todo_list)

    return todo_json
