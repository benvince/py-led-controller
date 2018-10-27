from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)   

@app.route('/')
def index():
    return "Hello world" 

@app.route('/zones', methods = ['POST', 'GET'])
def setup_zones():

    if(request.method == "POST"):
        for key, value in request.items():
            print(key)
        

    db = sqlite3.connect("data.sql")
    cur = db.cursor()

    cur.execute("SELECT * FROM ZONES")
    
    data = cur.fetchall()

    return(render_template("zones.html", zones = data))


if __name__ == "__main__":
   app.run('0.0.0.0', debug=True)


