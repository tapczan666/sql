# SELECT statement, remove Unicode characters

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	c.execute("SELECT firstname, lastname FROM employees")
	
	# fetchall() retrieves all records from the query
	rows = c.fetchall()

	# output the rows to the screen, row by row
	for r in rows:
		print(r[0], r[1])