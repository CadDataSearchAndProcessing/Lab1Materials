import pymongo
import sys
import json

def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.labs
    users_json_collection = db.users_json

    for i in json.loads(open('./dataset.json').read()):
        users_json_collection.insert(i)

if __name__ == "__main__":
    main()
