import sqlite3 
import hashlib
import sys

#make database connection
conn = sqlite3.connect("retail.db")
cur = conn.cursor()

#create admin table and products table
def create_table():
	conn = sqlite3.connect('retail.db')
	cur = conn.cursor()
	
	#check whether admin table exists or not. if it is not exists then create a admin table
	cur.execute("CREATE TABLE IF NOT EXISTS admin (admin_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT); ")
	cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER   PRIMARY KEY AUTOINCREMENT, name TEXT NPT NULL, price REAL NOT NULL, quantity INTEGER,discount  REAL);")
	
	cur.execute("SELECT * FROM admin")
	
	#check whether admin information exists or not. if it is not exists then asking admin info
	if cur.fetchone() is None:
		print("Plese insert admin details-------\n")
		adname = input("Enter admin's name: ")
		adpass = input("Enter password: ").encode()
		#hashing entered password  efore storing in the database
		hash_adpass = hashlib.md5(adpass).hexdigest()
		
		cur.execute("INSERT INTO admin (username, password) VALUES (?,?)",(adname, hash_adpass))
	
	print("Database has been created succesfully")
	conn.commit()
	

#login function	
def log_in():
	
	global conn
	global cur
	count=0
	while count<3:
		print("\n--------- Admin details ----------\n\n")
		uname = input("Enter your name: ")
		upass = input("Enter password: ").encode()
		hash_upass = hashlib.md5(upass).hexdigest()
	
		cur.execute("SELECT * FROM admin WHERE username = ? AND password= ? ", (uname, hash_upass))
		
		#verify admin login
		if cur.fetchone() is not None:
			print("Welcome "+uname+"!")
			return True
		else:
			print("Invalid user name or password,  try again!")
		count += 1
	
	print("Access denied!")

		
def userExit():
	uexit = input("Do u want to exit(yes/no)")
	if uexit.lower() in ("yes","y"):
		print("Successfully loged out")
		cur.close()
		conn.close()
		sys.exit()