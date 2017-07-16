import socket

clt_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1356
clt_sock.connect((host,port))
time = clt_sock.recv(1024)
clt_sock.close()
print "Time recieved from the server is", time.decode('ascii')

