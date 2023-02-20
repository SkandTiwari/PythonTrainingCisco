import socket
host = socket.gethostname()
port = 12345

s = socket.socket()
print("Welcome to test server 1 based on TCP socket connection")
print("Please enter the following credentials for echoback")
Name = input("Enter your name : ")
WifiConnBand = input("Enter your wifi band : ")
SSID_C = input("Enter SSID : ")

test_str = """Username : {} | Wifi Band : {} | SSID : {}""".format(Name, WifiConnBand, SSID_C)
test_data = bytes(test_str, 'utf-8')
s.connect((host, port))

s.sendall(test_data)

data = s.recv(1024)

print(data)
s.close()