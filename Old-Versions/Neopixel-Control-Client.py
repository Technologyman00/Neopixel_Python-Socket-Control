#!/usr/bin/env python

import socket
import sys
import webbrowser


TCP_IP = 'pi1792.local'
TCP_PORT = 5800
BUFFER_SIZE = 1024
nodata = 0
tryip = 1
good = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5801))

while True:

    #if tryip == 255:
       # print "Can't Find Server..."
       # TCP_IP = raw_input("Enter a Custom IP: ")
        #if TCP_IP == "":
          #  print "No Data Sent. Server Should Default Green."
           # break
       # print "Trying Ip: ", TCP_IP

    #if tryip == 256:
        #print "Custom IP FAILED. No Data Sent. Server SHOULD Default Green."
       # break

    #if tryip >= 2:
       # TCP_IP = '10.17.92.'
        #TCP_IP += str(tryip)
       # print "Trying Ip: ", TCP_IP

    while not good:
        MESSAGE = raw_input("Please enter a color: ")
        if MESSAGE == "":
            MESSAGE = "0,255,0"

        if "," in MESSAGE:
            print "you entered", MESSAGE
            good = True
            break
        else:
            print "Not a Color."

    try:
        print "Trying Again..."
        s.connect((TCP_IP, TCP_PORT))
    except Exception:
        nodata = 1
        if tryip == 1:
            print "Server not on pi1792.local... ERROR! Trying Again!"
        tryip += 1
    else:
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        s.close()
        nodata = 0
        print "RPI Found Address: ", TCP_IP
        text_file = open("Output.txt", "a")
        text_file.write("RPI IP: " + TCP_IP + "\r")
        text_file.close()
        print "RPI IP address saved to Output.txt"
        webbrowser.open(("http://" + TCP_IP + ":443"), new=0, autoraise=True)

    if nodata != 1:
        print "sent data:", data
        break
