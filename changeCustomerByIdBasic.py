import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["testData"]
mycol = mydb["customers"]

personToFind = mycol.find({'_id': ObjectId("633fdc5d9e39c2cab67b7c9c")})

print(personToFind)


myquery = {'_id': ObjectId("633fdc5d9e39c2cab67b7c9c")}
newvalues = { "$set": { "name": "test" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)