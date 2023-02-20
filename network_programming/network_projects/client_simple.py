import socket

sock = socket.socket()
host = socket.gethostname()
port = 9999
sock.connect((host, port))
text_data = "Request from Client"
sock.send(bytes(text_data, 'utf-8'))

rec_data = sock.recv(1024)
print("Response from server : ", rec_data)
sock.close()