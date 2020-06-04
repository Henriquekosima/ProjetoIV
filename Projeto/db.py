import sqlite3

conn = sqlite3.connect('DBprojeto.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE data (
	id INTEGER NOT NULL, 
	acc1 FLOAT, 
	acc2 FLOAT, 
	acc3 FLOAT, 
	gyro1 FLOAT, 
	gyro2 FLOAT, 
	gyro3 FLOAT, 
	countSteps FLOAT, 
	createdAt DATETIME, 
	PRIMARY KEY (id)
)
""")

conn.commit()
conn.close()