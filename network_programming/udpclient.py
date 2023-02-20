import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udphost = socket.gethostname()
udpport = 12345


msg = "Hello from client!"
print ("UDP target IP", udphost)
print ("UDP target Port", udpport)

sock.sendto(msg, (udphost, udpport))