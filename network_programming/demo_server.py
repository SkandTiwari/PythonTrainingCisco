import socket

sock = socket.socket()
host = socket.gethostname()
port = 9999

sock.bind((host, port))
sock.listen(5)

conn, addr = sock.accept()
while True:
    
    print("waiting for connection....")
    print("Connected by Host : ",addr)
    data = conn.recv(1024)
    if not data:
        print("no data received!")
        break
    print("data received from the client : ", data)
    while data:
        conn.sendall(data)
conn.close()
