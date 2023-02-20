import struct
import textwrap
import socket

def main():
    connection = socket.socket(socket.AF_PACKET, socket.SOCKET_RAW, socket.ntohs(3))
    print("Sniffing, please wait...")
    while True:
        rawData, address = connection.recvfrom(65535)
        reciever_mac, sender_mac, ethernetProtocol, data = ethernet_frame(rawData)
        print('Ethernet Frame: ')
        print('Destination: {}, Source: {}, Protocol: {}'.format(reciever_mac, sender_mac, ethernetProtocol))

def ethernet_frame(data):
    reciever_mac, sender_mac, protocol = struct.unpack('! 6s 6s H', data[:14])
    return getMacAddress(reciever_mac), getMacAddress(sender_mac), socket.htons(protocol), data[14:]

def getMacAddress(bytesAddress):
    bytesString = map('{:02x}'.format, bytesAddress)
    macAddress = ':'.join(bytesString).upper()
    return macAddress

main()