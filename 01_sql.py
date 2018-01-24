# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# crate a table
cursor.execute("""CREATE TABLE population
				(city TEXT, state TEXT, population INT)
				""")

# close the database connection
conn.close()