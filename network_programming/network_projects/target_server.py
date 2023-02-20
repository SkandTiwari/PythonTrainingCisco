import socket

sock = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 9999
print("IPv4 Address : ", ip)
sock.bind((host, port))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    print("waiting for connection....")
    data = conn.recv(1024)
    print(data)
    conn.close()