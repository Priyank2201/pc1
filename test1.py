import pymongo
client = pymongo.MongoClient("mongodb+srv://Last_man_standing:Rishu123@cluster0.6g3nwt6.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d={
    "name": "priyank",
    "gmail": "mail",
    "phone": "t"
}

db1 = client["mongotest"]
coll = db1["test1"]
coll.insert_one(d)