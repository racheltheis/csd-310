#Rachel Theis
#CSD310
#12.1.24

#This program runs queries on the films database using cursors in Python. 


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "f3!Xg8zA#7pL2Rkz",  # Random password, only used here 
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

db = None
cursor1 = None
cursor2 = None
cursor3 = None
cursor4 = None

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    cursor1 = db.cursor()
    cursor1.execute("SELECT * FROM studio")
    results1 = cursor1.fetchall()
    if results1:
        print("\n -- DISPLAYING Studio RECORDS --")
        for row in results1:
        	studio_id, studio_name = row
        	print(f"Studio ID: {studio_id} \nStudio Name: {studio_name}\n")
    else:
        print("No data found in the 'studio' table.")

    cursor2 = db.cursor()
    cursor2.execute("SELECT * FROM genre")
    results2 = cursor2.fetchall()
    if results2:
        print("\n -- DISPLAYING Genre RECORDS --")
        for row in results2:
        	genre_id, genre_name = row
        	print(f"Genre ID: {genre_id} \nGenre Name: {genre_name}\n")
    else:
        print("No data found in the 'genre' table.")


    cursor3 = db.cursor()
    cursor3.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    results3 = cursor3.fetchall()
    if results3:
        print("\n -- DISPLAYING Short Film RECORDS --")
        for row in results3:
        	film_name, film_runtime = row
        	print(f"Film Name: {film_name} \nRuntime: {film_runtime} \n")
    else:
        print("No data found for runs with a runtime of less than 120 minutes.")
        

    cursor4 = db.cursor()
    cursor4.execute("""
        SELECT film_name, film_director
        FROM film
        ORDER BY film_director;
    """)
    results4 = cursor4.fetchall()
    if results4:
        print("\n -- DISPLAYING Director RECORDS in Order --")
        for row in results4:
        	film_name, film_director = row
        	print(f"Film Name: {film_name} \nDirector: {film_director} \n")
    else:
        print("No data found for directors.")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    if cursor1 is not None:
        cursor1.close()
    if cursor2 is not None:
        cursor2.close()
    if cursor3 is not None:
        cursor3.close()
    if cursor4 is not None:
        cursor4.close()
    if db is not None:
        db.close()
        
#References
#GeeksforGeeks. (2018, December 14). Python | Output using print() function. GeeksforGeeks. 
#https://www.geeksforgeeks.org/python-output-using-print-function/MySQL. (n.d.). 
#MySQL :: MySQL Connector/Python Developer Guide :: 10.5 cursor.MySQLCursor Class. Dev.mysql.com. 
#https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html