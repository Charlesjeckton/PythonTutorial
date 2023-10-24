import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(5, 'EMOBILIS', 7,'WESTLAND', 25000.00)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(6, 'SAFARICOM', 20,'Kilimani', 30000.00)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(7, 'ORACLE', 15,'Karen', 150000.00)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(8, 'MICROSOFT', 32,'Kasarani', 270000.00)");

conn.commit()
print("Record created successfully")
conn.close()