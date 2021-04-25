from pymongo import MongoClient
'''
Creates an instance of the Mongodb client
'''
client = MongoClient("mongodb://localhost:27017")
DBName = client.TodoDB
todoList = DBName.todos
