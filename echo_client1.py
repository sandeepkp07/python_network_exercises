import socket
host = socket.gethostname()
port = 3542
clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clnt.connect((host,port))
a = raw_input()
clnt.sendall(a)
b = clnt.recv(1024)
print b
clnt.close()
