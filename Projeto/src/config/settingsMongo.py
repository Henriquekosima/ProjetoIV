""" from pymongo import MongoClient

client = MongoClient('mongodb+srv://henrique:<password>@cluster-s0ss5.mongodb.net/<dbname>?retryWrites=true&w=majority')

db = client.databaseMongo

registros = db.registros

registroDoc = {
    "id": ,
    "acc1": ,
    "acc2": ,
    "acc3": ,
    "gyro1": ,
    "gyro2": ,
    "gyro3": ,
    "countSteps": , 
    "createdAt":
    } """