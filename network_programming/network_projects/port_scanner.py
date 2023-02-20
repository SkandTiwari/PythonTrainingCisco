"""This is the demonstration project for network programming.

The project is based upon Port Scanner, basically demonstrates Socket programming upto some extent """

import socket

t_host = input("Enter the host to be scanned : ")

t_ip = socket.gethostbyname(t_host)

print(t_ip)

while True:
    t_port = int(input("Enter the port : "))
    try: 
        sock = socket.socket()
        sock.connect((t_ip, t_port))
        
        print("Port {}: Open".format(t_port))
        sock.close()
    except:
        
        print("Port {}: Closed".format(t_port))

print("Port Scanning complete")