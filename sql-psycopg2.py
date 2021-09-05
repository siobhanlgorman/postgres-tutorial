import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "Artist table"
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only the "Queen" column from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 3 - select only the "Queen" column from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', ["51"])

# query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 5 - select only the albums with "ArtistId" #51 column from the "Artist" column
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', ["51"])

# query 6 - select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# query 7 - select only the REM column from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["R.E.M."])

# query 8 - select only by "ArtistId" #124 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["R.E.M."])

# query 9 - select only the albums with "ArtistId" #124 column from the "Artist" column
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', ["124"])

# query 10 - select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["R.E.M."])

# query 11 - select all tracks where the composer is "test" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])


# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)