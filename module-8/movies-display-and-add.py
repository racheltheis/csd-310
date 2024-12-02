#Rachel Theis
#CSD310
#12.1.24

#This program prints a list of films, adds 'Us', and then reprints the list inclusive of 'Us'


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
    
    print("\n -- DISPLAYING FILMS --")
    show_films(cursor, "Film/Director/Genre/Studio Records")
    
    new_film_name = "Us"
    new_film_director = "Jordan Peele"
    new_film_genre_id = 1  
    new_film_studio_id = 3  
    new_film_runtime = 121 
    new_film_releaseDate = 2019
    
    new_film(new_film_name, new_film_director, new_film_genre_id, new_film_studio_id, new_film_runtime, new_film_releaseDate)
    
    print("\n --- DISPLAYING FILMS AFTER INSERT ---")
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
