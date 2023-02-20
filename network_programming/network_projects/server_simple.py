import socket

sock = socket.socket()
host = socket.gethostname()
port = 9999
sock.bind((host, port))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    print("Waiting for Connection...")
    print("Connection from : ", addr)
    data = conn.recv(1024)
    print("Request from client : ",data)
    text = "Hello from server"
    conn.send(bytes(text, 'utf-8'))
    conn.close()