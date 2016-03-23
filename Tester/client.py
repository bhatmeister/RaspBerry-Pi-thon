import socket

s = socket.socket()
<<<<<<< HEAD
host = '192.168.1.102'# ip of raspberry pi
=======
host = '192.168.1.108'# ip of raspberry pi
>>>>>>> origin/master
port = 12345
s.connect((host, port))
print(s.recv(1024))
s.close()
