

import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd = "H$8PjYFU",
    database = "movies"
)
mycursor = mydb.cursor()
print("\n  --  DISPLAYING FILMS --  ")
def show_films(mycursor,title):
    mycursor.execute("SELECT film_name AS Name,\
    film_director AS Director,\
    genre_name AS gENRE,\
    studio_name AS `Studio Name` FROM film \
    INNER JOIN genre ON film.genre_id = genre.genre_id \
    INNER JOIN studio ON film.studio_id = studio.studio_id")

    films = mycursor.fetchall()


    for film in films:
        print("Film Name: " + film[0])
        print("Director: " + film[1])
        print("Genre Name ID: " + film[2])
        print("Studio Name: " + film[3] + "\n")
show_films(mycursor, "Gladiator")


    #insert into film table a film of your choice
    #Avatar, James Cameron, (2)SciFi, (1)20th Century Fox, 162 minutes, 2009

insertNew = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s)"
movie1 = ("Avatar", 2009, 162, "James Cameron", 1, 2)

mycursor.execute(insertNew, movie1)

print("  --  DISPLAYING FILMS AFTER INSERT  --  ")

show_films(mycursor, "Gladiator")

mycursor.execute("UPDATE film SET genre_id = 1 WHERE film_id = 2")

print("\n  --DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror --  ")

show_films(mycursor, "Gladiator")

mycursor.execute("DELETE FROM film WHERE film_id = 1")

print("\n  -- DISPLAYING FILMS AFTER DELETE --  ")

show_films(mycursor, "Gladiator")



