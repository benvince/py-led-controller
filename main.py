from flask import Flask, render_template

app = Flask(__name__)   

@app.route('/')
def index():
    return "Hello world" 

@app.route('/setup')
def setup_stage():
    return("Setup Stage")


if __name__ == "__main__":
   app.run('0.0.0.0', debug=True)


