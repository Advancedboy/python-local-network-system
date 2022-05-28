from http import server
import socket
from sqlite3 import connect
from urllib import request, response

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5050))
server_socket.listen()
a = 1
while True:
	print('Before .accept()')
	client_socket, addr = server_socket.accept()
	print("Connection from", addr)

	while True:
		a +=1	
		print('Before .recv()')
		print(a)
		request = client_socket.recv(4096)

		if not request:
			break
		else:
			response = 'Hello world\n'.encode()
			client_socket.send(response)