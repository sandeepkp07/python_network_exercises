import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))
s.listen(10)
while True:
client, clnt_addr = s.accept()
print 'Connected from', clnt_addr
client.send("Connected")
client.close()
