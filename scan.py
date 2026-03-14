import os
import socket

print("Scanning")

os.system("ps")

for p in range(1,100):

    s = socket.socket()

    if s.connect_ex(("127.0.0.1",p)) == 0:
        print("Open",p)