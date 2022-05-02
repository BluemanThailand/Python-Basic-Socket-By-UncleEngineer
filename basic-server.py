#basic-server.py

import socket

serverip = 'localhost'
port = 7000

while True:
	server = socket.socket() # create socket
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # reuse old port 

	server.bind((serverip,port)) # can to run
	server.listen(5)  # recieved to server maximun 5 clients in same time
	print('Waiting for client...') 

	client, addr =server.accept() # who enter to this server accept auto
	print('Connect from:', str(addr))  
	data = client.recv(1024).decode('utf-8') # recieved data from client by decode 
	print('Message from client', data) 
	client.send('We received your Message!'.encode('utf-8')) # reply message 'We received your Message!'
	client.close()