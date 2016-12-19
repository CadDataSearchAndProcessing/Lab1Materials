import pymongo
import sys
import csv

def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.labs
    users_csv_collection = db.users_csv

    csvfile = open('./dataset.csv')
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip headers
    csvreader.__next__()

    for i in csvreader:
        users_csv_collection.insert({
            "id": i[0],
            "first_name": i[1],
            "last_name": i[2],
            "email": i[3],
            "gender": i[4],
            "ip_address": i[5]
        })

if __name__ == "__main__":
    main()
