# homework assignment No2

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# create a new table
	c.execute("CREATE TABLE orders (make TEXT, model TEXT, order_date DATE)")

	# populate the new table with data
	orders = [
			('Ford', 'F150', '2018-01-25'),
			('Ford', 'F150', '2017-11-11'),
			('Ford', 'F150', '2018-01-02'),
			('Ford', 'Escort', '2018-01-25'),
			('Ford', 'Escort', '2017-01-25'),
			('Ford', 'Escort', '2017-06-14'),
			('Ford', 'Focus', '2018-01-13'),
			('Ford', 'Focus', '2017-09-02'),
			('Ford', 'Focus', '2017-07-27'),
			('Honda', 'Jazz', '2018-01-06'),
			('Honda', 'Jazz', '2018-01-22'),
			('Honda', 'Jazz', '2018-01-01'),
			('Honda', 'Civic', '2017-04-02'),
			('Honda', 'Civic', '2017-01-25'),
			('Honda', 'Civic', '2016-03-16')]

	c.executemany("INSERT INTO orders VALUES (?,?,?)", orders)

	c.execute("SELECT * FROM orders ORDER BY order_date ASC")

	rows = c.fetchall()
	for r in rows:
		print(r[0], r[1], r[2])