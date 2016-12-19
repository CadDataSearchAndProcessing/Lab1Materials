import psycopg2
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
    #Define our connection string
    conn_string = "host='localhost' dbname='labs' user='postgres'"

    # print the connection string we will use to connect
    print("Connecting to database\n    ->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print("Connected!\n")

    for i in parseXML('dataset.xml'):
        query_string = """
            INSERT INTO users(id, first_name, last_name, email, gender, ip_address) VALUES (
                '{0}', '{1}', '{2}', '{3}', '{4}', '{5}'
            );
        """
        query = query_string.format(i['id'], i['first_name'], i['last_name'], i['email'], i['gender'], i['ip_address'])
        res = cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()


# create table users (id integer NOT NULL, first_name varchar,last_name varchar,email varchar,gender varchar,ip_address varchar);

if __name__ == "__main__":
    main()
