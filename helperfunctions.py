import mysql.connector
from config import username, password, host, database
from jobclasses import TABLES


def reset_db():
    # connect to mysql server
    client = loginToDB()

    # create the database if it does not exist
    create_database(client)
    cursor = client.cursor()

    # create each table from description in jobclasses.py
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == 1050:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    client.close()


def create_database(cnx):
    cursor = cnx.cursor()
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

    try:
        cursor.execute("USE {}".format(database))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(database))
        if err.errno == 1049:
            create_database(cursor)
            print("Database {} created successfully.".format(database))
            cnx.database = database
        else:
            print(err)
            exit(1)

    cursor.close()


def loginToDB():
    cnx = mysql.connector.connect(user=username, password=password,
                                  host=host,
                                  database=database)
    return cnx
