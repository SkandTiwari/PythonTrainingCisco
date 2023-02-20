import socket

sock = socket.socket()
host = socket.gethostname()
port = 12345

sock.connect((host, port))
tm = sock.recv(1024)

print("Current time from server is : ", tm)
sock.close()
 