
#CREATE TCP SCANNER

#CREATE UDP Scanner
#UDP has no 3 way hand shake, thus we cannot send SYN, ACK etc
#We send a packet wtih data, if we receive a response then the port is open

#from socket import *
from sys import *
import socket
from datetime import datetime

def getBanner(address,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        r=s.connect_ex((address,port))
        bruceBanner = s.recv(1024)
        s.close()
        #print("Service: ",bruceBanner)
        return bruceBanner
    except:
        #print("We cannot connect to port",port)
        return ("We cannot connect to port")
#host = argv[1]
host = "scanme.nmap.com"
#host="hackthissite.org"
#host="www.pleni.upd.edu.ph"
#host="202.92.128.181"
hostIP = socket.gethostbyname(host)

#hostIP = "192.168.1.1"
hostIP = "127.0.0.1"

#TCP SCAN
def TCPScan(address,port):
    #print("A")
    result = 1
    try:
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        r = s.connect_ex((hostIP,port))
        if r == 0:
            result = r
        s.close()
    except :
        pass
    return result

#print(s)
print(host)
print(hostIP)
#get start time
print("TCP SCAN")
# time1 = datetime.now()
# for port in range(1,200):
#     try:
#         TCPresponse = TCPScan(hostIP,port)
#         if TCPresponse == 0:
#             #print("TCP port %d is open"%port)
#             service = getBanner(hostIP,port)
#             print("TCP port %d is open. Service: %s"%(port,service))
#     except:
#             print("TCP port %d is close"%port)
#     #except:
#
# time2 = datetime.now()
# total = time2-time1
# print ("TCP Scan Time elapsed: ",total)

print("UDP SCAN")
#UDP SCAN
#Ref: https://pythontic.com/modules/socket/udp-client-server-example
UDPSocket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(UDPSocket)
for port in range (1,10000):
    try:
        data = "Hello"
        print(UDPSocket.sendto(data,(host,port)))
        UDPSocket.settimeout(2)
        print ((UDPSocket.recvfrom(1024)))
    except:
        pass

    #if(UDPSocket.connect_ex((host,port))==0):
    #    print("UDP port %d is open"%port)
    #else:
    #    print("UDP port %d is closed"%port)
