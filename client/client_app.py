#!/usr/bin/python

class LED_Client():

    num_leds = 0 
    zone_name = ""

    def __init__(self):

        self.num_leds = 10

    
    def draw_out(self):
        
        print("[*] "  * self.num_leds)


a = LED_Client()
a.zone_name = "Conservatory"
a.num_leds = 10
a.draw_out()



