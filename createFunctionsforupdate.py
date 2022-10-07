import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")



#en funktion där man med hjälp av _id kan hitta ett specifikt dokument och ändra valfritt attribut i det
def updateDocumentById(databaseToUpdate:str, collectionToUpdate:str ,idToUpdate:str, valueToUpdate:str, newValue:str):
    database = myclient[databaseToUpdate]
    collection = database[collectionToUpdate]
    query = {'_id': ObjectId(idToUpdate)}
    newvalues = { "$set": { valueToUpdate: newValue } }
    collection.update_one(query, newvalues)


# updateDocumentById("testData", "customers", "633fdc5d9e39c2cab67b7c9c", "name", "Robert")
# updateDocumentById("testData", "customers", "633fdc5d9e39c2cab67b7c9c", "address", "Sigurdsgatan 20")

