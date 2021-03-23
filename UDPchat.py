import socket
import os
import time
import threading
import sys


def receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip_sender, port_sender))
    while True:
        msg = sock.recvfrom(1024)
        print("\n"+msg[0].decode())
        if "exit" in msg[0].decode() or "bye" in msg[0].decode():
            sys.exit()


def sender():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = "hello"
    while True:
        if "bye" in text or "exit" in text or "finish" in text:
            exit()
        else:
            text = input(f'{name}:')
            text = name+":"+text
            s.sendto(text.encode(), (ip_receiver, port_receiver))


print("Initializing....")
ip_receiver = input("\nEnter the IP of reciever: ")
port_receiver = int(input("\nEnter the port of the reciever: "))
ip_sender = input("\nEnter the IP of your system : ")
port_sender = int(input("\nEnter the port of your system: "))
name = input("Please enter your name: ")


print("Waiting for client....")
time.sleep(1)
print("Connection established....")


send = threading.Thread(target=sender)
recieve = threading.Thread(target=receiver)
send.start()
recieve.start()
