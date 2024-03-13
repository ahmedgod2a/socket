import threading
import socket
import time

PORT = 7070
FORMAT = "utf-8" #type of write
D = "DES"
HEADER = 64 #size of message
SERVER = "192.168.174.1" #ip adderss of server
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    MSG = msg.encode(FORMAT)
    msg_len = len(MSG)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(MSG)

def read():
    msg_len = conn.recv(HEADER).decode(FORMAT)
    if msg_len:
        msg_len = int(msg_len) #size of message will come
        msg =client.recv(msg_len).decode(FORMAT) # recve message and utf-8  
        print(f"{msg}")    
    

x = ''

while 1:
    input (x)
    if x !=(D):
        send(x)
    thread = threading.Thread(target=read )
    thread.start() 

send(D)
