import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	