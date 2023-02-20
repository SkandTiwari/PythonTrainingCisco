import socket

sock = socket.socket()

host = socket.gethostname()
sock.connect((host, 12345))
sock.setblocking(0)

# This line is simply blocking, there's no need for putting this line in here as TCP sockets are always in blocking mode

data = "Hello Python\n" *10*1024*1024
assert sock.send(bytes(data, 'utf-8'))