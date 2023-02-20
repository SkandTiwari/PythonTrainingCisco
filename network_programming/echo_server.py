import socket

host = socket.gethostname()
port = 12345
s = socket.socket()
s.bind((host, port))
s.listen(5)

print("Waiting for connection....")

conn, addr = s.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
