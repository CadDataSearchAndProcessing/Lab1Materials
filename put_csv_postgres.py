import psycopg2
import sys
import csv

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

    csvfile = open('./dataset.csv')
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip headers
    csvreader.__next__()

    for i in csvreader:
        query_string = """
            INSERT INTO users_csv(id, first_name, last_name, email, gender, ip_address) VALUES (
                '{0}', '{1}', '{2}', '{3}', '{4}', '{5}'
            );
        """
        query = query_string.format(i[0], i[1], i[2], i[3], i[4], i[5])
        res = cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()


# create table users (id integer NOT NULL, first_name varchar,last_name varchar,email varchar,gender varchar,ip_address varchar);

if __name__ == "__main__":
    main()
