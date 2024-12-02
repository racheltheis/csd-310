#Rachel Theis
#CSD310
#12.1.24

#This program displays the film list after a genre update, deletes a film, then displays the updated film list

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "f3!Xg8zA#7pL2Rkz",  
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

db = None
cursor = None

#adding delete function
def delete_film(film_name):
    try:
        query = "DELETE FROM film WHERE film_name = %s"
        cursor.execute(query, (film_name,))
        db.commit()
        print(f"Film '{film_name}' deleted successfully.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def show_films(cursor, title):
    cursor.execute("""
    SELECT film_name AS Name, 
           film_director AS Director, 
           genre_name AS Genre, 
           studio_name AS 'Studio Name' 
    FROM film 
    INNER JOIN genre ON film.genre_id = genre.genre_id 
    INNER JOIN studio ON film.studio_id = studio.studio_id
    """)
    
    films = cursor.fetchall()
    
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio: {}\n".format(film[0], film[1], film[2], film[3]))
        

def new_film(film_name, film_director, genre_id, studio_id, film_runtime, film_releaseDate):
    query = """
    INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime, film_releaseDate)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (film_name, film_director, genre_id, studio_id, film_runtime, film_releaseDate))
    db.commit()

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()
     #already changed genre in MySQL   
    print("\n --- DISPLAYING FILMS AFTER UPDATE -Changed Alien to Horror ---")
    show_films(cursor, "Film/Director/Genre/Studio Records")
    
    #deleting gladiator
    delete_film('Gladiator')
    
    print("\n -- DISPLAYING FILMS AFTER DELETE --")
    show_films(cursor, "Film/Director/Genre/Studio Records")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    if cursor is not None:
        cursor.close()
    if db is not None:
        db.close()
