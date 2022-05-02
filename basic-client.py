#basic-client.py

import socket

serverip = 'localhost'
#serverip = '159.65.135.242' # Uncleengineer.com
port = 7000

while True:
	data = input('Enter Message: ') # input data
	server = socket.socket() # create socket
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # reuse old port 

	server.connect((serverip,port)) # connect server and port follow 
	server.send(data.encode('utf-8')) # send data to server before send encode to byte

	data_server = server.recv(1024).decode('utf-8') # recieved data from server
	print('Data from Server:', data_server)
	server.close()                                                                                                                                                                                                                                                                                                                                                                                                    