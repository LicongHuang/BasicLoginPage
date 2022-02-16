from __future__ import print_function
from datetime import date, datetime
import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(user='root',host='localhost',password="",database="login")
cursor=mydb.cursor(buffered=True)

date = datetime.now().date()


def user_input():
	username = input("Input your username: ")
	password = input("Input your password: ")
	try:
		if add_info(username,password) == False:
			user_input()
		else:
			return False

	except:
		print("THERE IS A PROBLEM ADDING YOUR USERNAME")
		user_input()


def add_info(urnm,pswd,date=date,priv=0,active='1'):
	add_login = ("INSERT INTO login_info"
				"(username,password)"
				" VALUES (%s,%s)"
		)

	add_acc = ("INSERT INTO acc_info"
				"(user_id,create_date,priviledge,active)"
				" VALUES (%s,%s,%s,%s)"
		)

	login_data = (urnm,pswd)
	try:
		cursor.execute(add_login,login_data)
		acc_data = (cursor.lastrowid,date,priv,active)
		cursor.execute(add_acc,acc_data)
		mydb.commit()
		print("Data added")
	except :
		mydb.rollback()
		print("This Username has already been used, please try a new one.")
		return False


def find_info(urnm):
	cursor.execute("SELECT * from `login_info` where `username` = '{}';".format(urnm))
	row = cursor.fetchone()
	print("Checking")
	if row is not None:
		return True
	return False
	 

def verification(urnm,pwd):
	find_user=("SELECT `user_id` FROM `login_info` WHERE username = '{}';".format(urnm))
	find_pwd=("SELECT `user_id` FROM `login_info` WHERE username = '{}';".format(pwd))
	cursor.execute(find_user)
	row = cursor.fetchone()
	if row is not None:
		cursor.execute(find_pwd)
		row2=cursor.fetchone()
		print("Row2 is : ", row2)
		if row2 is not None:
			return True
	return False

def edit_login(urnm,newpswd):
	data = (newpswd,urnm)
	#find_user=("SELECT `user_id` FROM `login_info` WHERE username = '{}';".format(urnm))
	update_user=("UPDATE `login_info` SET `password`=%s WHERE username=%s;")
	try:

		cursor.execute(update_user,data)
		mydb.commit()
		print("Updated")
	except Error as error:
		mydb.rollback()
		print("Problem updating")

def delete_info(urnm):
	find_id=("SELECT `user_id` FROM `login_info` WHERE username = '{}';".format(urnm))
	cursor.execute(find_id)
	row = cursor.fetchone()
	delete_single(row[0])
		


def delete_single(dig):
	try:
		delete_item = ("DELETE FROM `login_info` WHERE `user_id`={}".format(dig))
		cursor.execute(delete_item)
		mydb.commit()
		print("Item deleted")
	except:
		mydb.rollback()
		print("Problem deleting")
		#INPUT QUERY FUNCTIONS

if __name__ == '__main__':
	#add_info("Name","Password")
	edit_login("Name","Password2")
#delete_info("Name")
#while user_input():
#	user_input()

#cursor.execute("SELECT * from `login_info`;")

#cursor.close()
#mydb.close()
