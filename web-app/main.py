#!/bin/python

from flask import Flask, render_template, request
import sqlite3


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


if __name__ == "__main__":
   app.run('0.0.0.0', debug=True)


