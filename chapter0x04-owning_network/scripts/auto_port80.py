from scapy.all import *
import socket
import os



def grab_requests(packet):
    source = packet["IP"].src
    dest = packet["IP"].dst
    try:
        dns = socket.gethostbyaddr(dest)
        print(f'{source} -> {dest} | {dns} ')
    except:
        pass
    


sniff(filter="tcp port 80 or tcp port 443",prn=grab_requests,count=100 )
