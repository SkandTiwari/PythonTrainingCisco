import socket
import time

sock = socket.socket()
host = socket.gethostname()
port = 12345

sock.bind((host, port))

sock.listen(5)

while True:
    conn, addr = sock.accept()
    print("waiting for connection....")
    print("we got a connection from : ", addr)
    tm = str(time.ctime(time.time()))
    conn.send(bytes(tm, 'utf-8'))
    conn.close()