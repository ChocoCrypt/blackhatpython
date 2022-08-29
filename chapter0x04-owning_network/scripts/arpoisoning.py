from scapy.all import *
import os
import sys
import threading
import signal



interface = "wlp1s0"
target_ip = "192.168.0.109"
gateway = "192.168.0.9"


conf.iface = interface
conf.verv = 0


print(get_mac(target_ip))
