#Rachel Theis
#CSD310
#11.23.24

#This program was taken from the CSD310 Module 6.2 instructions to connect the "movies" DB with Python


import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "root",
	"password": "f3!Xg8zA#7pL2Rkz", #random password, only used here 
	"host": "localhost",
	"database": "movies",
	"raise_on_warnings": True

}

db = None

try:
	db = mysql.connector.connect(**config)
	
	print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
	
	input("\n\n  Press any key to continue... ")
	
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  The supplied username or password are invalid")
		
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specified database does not exist")
		
	else:
		print(err)
		
finally:
	if db is not None:
		db.close()