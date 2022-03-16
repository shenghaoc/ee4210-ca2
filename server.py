from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(1024).decode()
    print(request)
    headers = request.split('\r\n')
    filename = headers[0].split()[1]
    if filename == '/':
        filename = '/index.html'
    connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
    connectionSocket.sendfile(open('.' + filename, "rb"))
    connectionSocket.close()
