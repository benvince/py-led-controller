#!/usr/bin/python

import socket
import json
from flask import Flask, request
import RPi.GPIO as GPIO


PORT_NUMBER = 7878

class LED_Client():

    config = {}

    def __init__(self, config_file):

        self.load_config(config_file)

    def load_config(self, config_file):

        with open(config_file, "r") as f:
            self.config = json.loads(f.read())

    def draw_out(self):
        print("Zone Name: {}".format(self.config['zone_name']))         
        print("[*] "  * self.config['num_leds'])

a = LED_Client("config.json")
app = Flask(__name__)

@app.route("/api/get_config/")
def get_config():
    return(json.dumps(a.config))

@app.route("/api/toggle_light")
def toggle_light():
    
    pin = config.config['pin_no']
    toggle_pin(pin)

    return("Done")

@app.route("/api/toggle_pin/<int:pin>", methods = ['GET'])
def toggle_pin(pin):

    #print("TOGGLE PIN {}".format(pin))
    GPIO.output(pin,not bool(GPIO.input(pin))) ## Turn on GPIO pin 7
   
    return("Done")

if __name__ == "__main__":
    
    config = LED_Client('config.json')

    OUT_PINS = []
    IN_PINS = []

    OUT_PINS.append(config.config['pin_no'])

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(OUT_PINS, GPIO.OUT)
    GPIO.setup(IN_PINS, GPIO.IN)

    app.run('0.0.0.0', port = PORT_NUMBER,  debug=True)

