import pymongo
import sys
import xml.etree.ElementTree as ET

def parseXML(file):
    tree = ET.parse(file)
    root = tree.getroot()

    result = []

    for record in root.findall('record'):
        result.append({
            'id': record.find('id').text,
            'first_name': record.find('first_name').text,
            'last_name': record.find('last_name').text,
            'email': record.find('email').text,
            'gender': record.find('gender').text,
            'ip_address': record.find('ip_address').text
        })

    return result

def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.labs
    users_xml_collection = db.users_xml

    for i in parseXML('dataset.xml'):
        users_xml_collection.insert({
            "id": i["id"],
            "first_name": i["first_name"],
            "last_name": i["last_name"],
            "email": i["email"],
            "gender": i["gender"],
            "ip_address": i["ip_address"]
        })

if __name__ == "__main__":
    main()
