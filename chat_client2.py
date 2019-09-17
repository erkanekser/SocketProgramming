import time
from datetime import datetime
import socket
import threading
from tkinter import *

root = Tk()
root.title("rf-Hotel TV")
text = Text(master=root, bg="Cyan")
text.pack(expand=True, fill="both")

udp_port = 5005
udp_ip = str(socket.gethostbyname(socket.gethostname()))
a = len(udp_ip)
for i in range(0, a):
    if udp_ip[a - i - 1] == ".":
        udp_ip = udp_ip[:(a - i)] + "255"
        break

class Client:
    def send(self):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = 'Hi server'
        self.__sock.sendto(message.encode('utf-8'), (udp_ip, udp_port))

    def receive(self):
        self.__sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock2.bind((socket.gethostbyname(socket.gethostname()),5006))
        self.__sock2.listen(5)
        while True:
            connecting, receivingip = self.__sock2.accept()
            data=connecting.recv(8192)
            now = str(datetime.now())[:-7]
            text.insert("insert", "Message: {} / Date: {} / \n".format(data.decode(), now))

c1 = Client()

def send():
    t1 = threading.Thread(target=c1.send)
    t1.start()

def SearchingServerControl():
    t2 = threading.Thread(target=c1.receive)
    t2.start()

SearchingServerControl()

button_send = Button(text="Search", command=send)
button_send.pack(expand=True)

t0 = threading.Thread(target=root.mainloop)
t0.run()