#!/usr/bin/python

import socket
import json
from flask import Flask, request

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

if __name__ == "__main__":

    app.run('0.0.0.0', port = PORT_NUMBER,  debug=True)

