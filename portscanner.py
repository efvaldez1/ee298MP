
#CREATE TCP SCANNER



#CREATE UDP Scanner
#UDP has no 3 way hand shake, thus we cannot send SYN, ACK etc
#We send a packet wtih data, if we receive a response then the port is open

from socket import *
from sys import *


print("2nd args is the host IP")
#host = argv[1]
host = "scanme.nmap.com"
#host="www.pleni.upd.edu.ph"
host="202.92.128.181"
port = 5

s= socket(AF_INET,SOCK_STREAM)
#host = s.gethostbyname("www.scanme.nmap.com")
print(s)
print(host)
print(s.connect_ex((host,port)))
for port in range(1,162):
    if(s.connect_ex((host,port))==0): # successful
        print("port %d is open"%port)
    else:
        print("port %d is close"%port)
