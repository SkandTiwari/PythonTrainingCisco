import socket

sock = socket.socket()
host = socket.gethostname()
port = 9999

sock.connect((host, port))
data = "this is the data to be echoed back from the server"
sock.sendall(bytes(data, 'utf-8'))
rec_data = sock.recv(1024)
print(rec_data)
sock.close()
