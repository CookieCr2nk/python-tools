#create a script that check if a port is open or not
#this script will be used to check if a port is open or not

import socket

host = 1.1.1.1
port = 80
s = 0

def portScanner(port):
    if s.connect_ex((host,port)):
        print("The port is closed")
    else:
        print("The port is open")