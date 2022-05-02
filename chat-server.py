#chat-server.py

import socket
import datetime
import threading

PORT = 7500 # create new port
BUFSIZE = 4096 # define size to message limit 4096
SERVERIP = '192.168.88.130' # your ip

clist = [] # client list
cdict = {}

def client_handler(client,addr):
	while True:
		try:
			data = client.recv(BUFSIZE)
			check = data.decode('utf-8').split('|')
			if check[0] == 'NAME':
				cdict[str(addr)] = check[1]

		except:
			clist.remove(client)
			break

		if (not data) or (data.decode('utf-8') == 'q'):
			clist.remove(client)
			print('OUT: ', client)
			break
		try:
			username + cdict[str(addr)]
			msg = username + '>>> ' + data.decode('utf-8')
		except:
			msg = str(addr) + '>>> ' + data.decode('utf-8') # message send to all client
		print('USER: ',msg)
		print('---------')

		try:
			check =data.decode('utf-8').split('|')
			if check[0] == 'NAME':
				pass
			else:
				for c in clist:
					c.sendall(msg.encode('utf-8'))
		except:
			for c in clist:
					c.sendall(msg.encode('utf-8'))

	client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new server
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # reuse old port
server.bind((SERVERIP,PORT)) # turn on server
server.listen(5) # define number of client limit 5 client connect to server as the same time

while True:
	client, addr =server.accept() # who enter to this server accept auto
	clist.append(client) # add client record to clist
	print('ALL CLIENT: ', clist)  # print client

	task = threading.Thread(target=client_handler, args=(client,addr)) # create threading
	task.start()

