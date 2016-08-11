#!/usr/bin/env python

import socket
from neopixel import *

print "Starting Neopixel Control Server."
# Neopixel Variables
LED_COUNT = 12  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()

# Server Variables
TCP_IP = '0.0.0.0'
print "Sever IP is: ", TCP_IP, " or ", socket.gethostname()
TCP_PORT = 5800
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

#Color Variables
color = ""
Red = "0"
Green = "255"
Blue = "0"

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    color = data
    conn.send(data)  # echo
conn.close()

#Color Choosing
Red, Green, Blue = color.split(",")
print "Red: ", Red
print "Green: ", Green
print "Blue: ", Blue
for i in range(0,LED_COUNT):
    strip.setPixelColor(i, color(Red, Green, Blue))
strip.show()
