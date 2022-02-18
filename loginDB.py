#im trying to do shit, i think
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

DB_NAME = "login";

TABLES = {}

#login_info(user_id*,username,password)
TABLES["login_info"]=(
    "CREATE TABLE `login_info` ("
    " `user_id` int(4) NOT NULL AUTO_INCREMENT,"
    " `username` varchar(16) NOT NULL ,"
    " `password` varchar(16) NOT NULL,"
	" UNIQUE(`user_id`),"
	" UNIQUE(`username`),"
    " PRIMARY KEY (`user_id`)"
    ") ENGINE=InnoDB"
)

#acc_info(user_id*#,priviledges,creation_date,active)
TABLES["acc_info"]=(
    "CREATE TABLE `acc_info` ("
    " `user_id` int(4),"
    " `priviledges` int(1) NOT NULL,"
    " `creation_date` date NOT NULL,"
    " `active` enum('0','1') NOT NULL,"
    " PRIMARY KEY (`user_id`),"
    " FOREIGN KEY (`user_id`) REFERENCES login_info(`user_id`)"
    " ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)


mydb = mysql.connector.connect(user='root',host='localhost',password='')
cursor = mydb.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        mydb.database=DB_NAME
    else:
        print(err)
        exit(1)

for table_name  in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}:".format(table_name),end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Already Exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
mydb.close()        