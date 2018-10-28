#!/usr/bin/python

import socket
import json
from flask import Flask, request
import RPi.GPIO as GPIO

PORT_NUMBER = 7878

#Read in config:-
config = json.loads(open("config.json").read())
app = Flask(__name__)

@app.route("/api/get_config/")
def get_config():
    return(json.dumps(config))

@app.route("/api/toggle_light")
def toggle_light():
    
    pin = config['pin_no']
    toggle_pin(pin)

    return("Done")

@app.route("/api/toggle_pin/<int:pin>", methods = ['GET'])
def toggle_pin(pin):

    GPIO.output(pin,not bool(GPIO.input(pin))) ## Turn on GPIO pin 7
   
    return("Done")

if __name__ == "__main__":
    
    OUT_PINS = []
    IN_PINS = []

    OUT_PINS.append(config['pin_no'])

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(OUT_PINS, GPIO.OUT)
    GPIO.setup(IN_PINS, GPIO.IN)

    app.run('0.0.0.0', port = PORT_NUMBER,  debug=True)

