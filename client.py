from socket import *

serverName = 'localhost'
serverPort = 12000

# First client socket to request HTML file
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send('GET /index.html HTTP/1.0\r\n'.encode())
response = clientSocket.recv(1024).decode()
clientSocket.close()
print(response)

# Second client socket to request txt file
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send('GET /bio.txt HTTP/1.0\r\n'.encode())
response = clientSocket.recv(1024).decode()
clientSocket.close()
print(response)
