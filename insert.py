import sqlite3 as sql
import time
local_time = time.asctime(time.localtime(time.time()))
print(local_time)
with sql.connect("database.db") as con:
    cur=con.cursor()
    print("Herre")
    
    cur.execute("INSERT INTO JeebleMacAdd(macAddress,timestamp) VALUES(?,?)",("225-2-5-2-5-2",str(local_time),))
    cur.execute("SELECT * from JeebleMacAdd WHERE macAddress = '225-22-5-2-5-2' ")
    cur.execute("INSERT INTO Log(macAddress,status,timestamp) VALUES(?,?,?)",("225-2-5-2-5-2","Login",str(local_time),))
    #cur.execute("IF EXISTS ()")
    rows=cur.fetchall()
    print(len(rows))
    cur.close()
    #print(rows[1][0])
    
    print("Open data base successfully")
    print("Table Created Successfully")
#    con.close()

