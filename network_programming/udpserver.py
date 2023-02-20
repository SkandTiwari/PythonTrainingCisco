import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udphost = socket.gethostname()
udpport = 12345

sock.bind((udphost, udpport))

while True:
    print("waiting for network...")
    data, addr = sock.recvfrom(1024)
    print("Received Messages : ", data, " from", addr)
