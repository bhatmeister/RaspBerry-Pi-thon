import socket

s = socket.socket()
host = '192.168.1.48' #ip of raspberry pi
port = 13000
s.bind((host, port))

print ("Server Listening at /(host)",host)

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.send('Thank you for connecting')
  c.close()
