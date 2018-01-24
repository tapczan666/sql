import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# crate a list of cars to insert into the database
	cars = [
		('Ford', 'F150', 100),
		('Ford', 'Escort', 11),
		('Ford', 'Focus', 72),
		('Honda', 'Jazz', 83),
		('Honda', 'Civic', 55)
		]

	# insert the cars into the database
	c.executemany("INSERT INTO inventory VALUES (?, ?, ?)", cars)

	# update the quantity on two records
	c.execute("UPDATE inventory SET Quantity = 99 WHERE Model = 'F150'")
	c.execute("UPDATE inventory SET Quantity = 99 WHERE Model = 'Civic'")

	# output all the records
	print("\nALL VEHICLES:\n")
	c.execute("SELECT * FROM inventory")
	rows = c.fetchall()
	for r in rows:
		print(r[0], r[1], r[2])

	# output only Ford vehicles
	print("\nFORD VEHICLES:\n")
	c.execute("SELECT * FROM inventory WHERE Make = 'Ford'")
	rows = c.fetchall()
	for r in rows:
		print(r[0], r[1], r[2])