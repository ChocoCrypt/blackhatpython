import socket
import os

# Target:
host = "192.168.0.109"


protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW , protocol)
sniffer.setsockopt(socket.IPROTO_ICMP,socket.IP_HDRINCL ,1 )



print(sniffer.recvfrom(65535))
