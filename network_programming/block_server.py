import socket

sock = socket.socket()
hostname = socket.gethostname()
port = 12345

sock.bind((hostname, port))
sock.listen(5)

while True:
    conn, addr = sock.accept() #Accept the connection

    data = conn.recv(1024)
    while data:         #Till data is coming
        
        print(data)
        data = conn.recv(1024)
    print("All data received!")  #Print till all data is received

    conn.close()
    break