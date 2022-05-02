#chat-client.py

import socket
import datetime
import threading
import sys

PORT = 7500 # create new port
BUFSIZE = 4096 # define size to message limit 4096
SERVERIP = '192.168.88.130' # server ip


def server_hanler(client):
	while True:
		try: 
			data = client.recv(BUFSIZE) # data from server
			
		except:
			print('ERROR!')
			break
		if (not data) or (data.decode('utf-8') == 'q'):
			print('OUT!')
			break

		print('USER: ', data.decode('utf-8')) # if have data from server print output


	client.close()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new client
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # reuse old port


try: # try connect to server
	client.connect((SERVERIP,PORT)) 
except:
	print('ERROR!')
	sys.exit() # can't connect exit to system

task = threading.Thread(target=server_hanler, args=(client,)) # create threading
task.start()

while True:
	msg = input('Message: ') # input massage
	client.sendall(msg.encode('utf-8')) # encode from massage to byte
	if msg == 'q':
		break
client.close()
