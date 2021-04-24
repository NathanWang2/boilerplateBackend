from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
DBName = client.TodoDB
todoList = DBName.todos
