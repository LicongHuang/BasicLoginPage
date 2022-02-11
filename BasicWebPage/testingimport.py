import insertsql 
import mysql.connector

mydb = mysql.connector.connect(user='root',host='localhost',password="",database="login")
cursor=mydb.cursor(buffered=True)

insertsql.find_info("name")

cursor.close()
mydb.close();
