# homework assignment No2 - continued

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# find all car models in the inventory
	c.execute("SELECT * FROM inventory")
	inventory = c.fetchall()

	for car in inventory:
		print(car[0], car[1])
		print(car[2])

		# find all order dated for a given model
		c.execute("SELECT order_date FROM orders WHERE make = ? AND model = ? ORDER BY order_date", (car[0], car[1]))
		dates = c.fetchall()
		for d in dates:
			print(d)