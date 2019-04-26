
from flask import Flask, redirect, url_for, request
import sqlite3 as sql
from random import randint
import time
from flask import jsonify

local_time = time.asctime(time.localtime(time.time()))

app = Flask(__name__)

@app.route('/required_jeebler_micro',methods = ['POST', 'GET'])
def required_jeebler_micro():
   if request.method == 'POST':
       
      #user = request.headers
      #print(user)
      #json_p = request.get_json()
      user = request.get_json()
      print(user)
      res_str = str(randint(1,10))
      return jsonify(message = res_str)
   else:
      return "Error Sending Request, try again."

      #user = request.args.get('nm')
      #return "error in post"#redirect(url_for('success',name = user))


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/required_jeebler',methods = ['POST', 'GET'])
def required_jeebler():
   if request.method == 'POST':
       
      #user = request.headers
      #print(user)
      #json_p = request.get_json()
      #user = request.get_json()
      #print(user)
      
      response = "Please Confirm. ETA-"+str(randint(1,10))+" min." 
      #print(json_p["sensor"])   
      return response
   else:
      return "Error Sending Request, try again."

      #user = request.args.get('nm')
      #return "error in post"#redirect(url_for('success',name = user))

@app.route('/confirm_jeebler',methods = ['POST', 'GET'])
def confirm_jeebler():
   if request.method == 'POST':
      #user = request.get_data()
      #print(user)
    
      return "Jeebler on the way!"
   else:
      user = request.args.get('nm')
      return "error in post"#redirect(url_for('success',name = user))


@app.route('/send_macaddress',methods = ['POST', 'GET'])
def send_macaddress():
   if request.method == 'POST':
      try:
          user = request.get_json()
          #user = request.form['yourdata']
          print(type(user), " ", len(user) )
          print(user['Minor']," ", user['Major'] )
          mac_add = str(user['Minor']) + str(user['Major'])
          print(mac_add)
          #print(rows[1][0])
          #mgs = "Jeebler is on the way!"# + str(rows['log'])
          mgs =  check_macaddress(mac_add,str(user['Minor']))
          
      except Exception as e:
          print(e)
          mgs = "Error in insert operations."
      finally:
          
          print("here is the return message: ",mgs)
          return mgs
   else:
      return "error in post"

def check_macaddress(user_macaddress,minor):
    print(type(user_macaddress))
    with sql.connect("database.db") as con:
        cur = con.cursor()
        select_query = "SELECT * from JeebleMacAdd WHERE macAddress = " + str(user_macaddress )
        cur.execute(select_query)
        rows=cur.fetchall()
        if (len(rows) == 1):
            delete_query = "DELETE FROM JeebleMacAdd WHERE macAddress = '"+user_macaddress+"'"
            cur.execute(delete_query)
            cur.execute("INSERT INTO Log(macAddress,status,timestamp) VALUES(?,?,?)",(str(user_macaddress),"Logout",str(local_time),))
            print("Logout")
            response = "Driver-"+minor+" logged out."
            
        elif (len(rows) == 0):
            cur.execute("INSERT INTO JeebleMacAdd(macAddress,timestamp) VALUES(?,?)",(str(user_macaddress),str(local_time),)) 
            cur.execute("INSERT INTO Log(macAddress,status,timestamp) VALUES(?,?,?)",(str(user_macaddress),"Login",str(local_time),)) 
            print("Login")
            response = "Driver-"+minor+" Logged IN"
            
        else:
            print("More than one entry exists")
            response = "Error database"            
    return response

@app.route('/test_get',methods = ['GET'])
def test_get():
    return "Server up and running."

if __name__ == '__main__':
   app.run(debug = True)
   