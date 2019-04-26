import sqlite3

conn = sqlite3.connect( 'database.db')
print ("Open database successfully")
conn.execute('CREATE TABLE Log (macAddress int, status varchar(255), timestamp varchar(255))')
conn.execute( 'CREATE TABLE JeebleMacAdd (macAddress varchar(255), timestamp varchar(255))')
print("Table Created Successfully")
conn.close()
