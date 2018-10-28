#!/bin/python

from flask import Flask, render_template, request
import sqlite3
import requests
import json

app = Flask(__name__)   

@app.route('/')
def index():
    return "Hello world" 

@app.route('/zones', methods = ['POST', 'GET'])
def setup_zones():
    
    #Connect to DB:-
    db = sqlite3.connect("data.sql")
    cur = db.cursor()
   
   #If posting, store new zone into database:-
    if(request.method == "POST"):
        for key, value in request.items():
            print(key)
        

    #Get Zones from Database:-
    cur.execute("SELECT * FROM ZONES")
    data = cur.fetchall()
    
    #Return zones.html template and pass zone data from db to it:-
    return(render_template("zones.html", zones = data))

@app.route("/all_zone_configs")
def all_zones():
 
    #Connect to DB:-
    db = sqlite3.connect("data.sql")
    cur = db.cursor()

    #Get Zones from Database:-
    cur.execute("SELECT zone_ip, zone_port FROM ZONES")
    data = cur.fetchall()
   
    html = ""
        

    for zone_ip, zone_port in data:
        
        try:
            zone_config = requests.get("http://{}:{}/api/get_config".format(zone_ip,
                                                          zone_port))

            config = json.loads(zone_config.text)
            html += "<b> Zone Address: {}:{}<br></b> ".format(zone_ip, zone_port)
            html += "Zone Name: {}</br>".format(config['zone_name'])
            html += "No. of LEDs: {}".format(config['num_leds'])
 
        except:
            html += "Can't connect to {}:{}".format(zone_ip, zone_port)

    return(html) 



if __name__ == "__main__":
   app.run('0.0.0.0', debug=True)


