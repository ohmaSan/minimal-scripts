#!/usr/bin/python3
# Tokuchi Toua
# cportchecker.py (Python3 Spesific Port Checker)
# One packet sender spesific port!

from scapy.layers.inet import TCP, IP
from scapy.all import *
import time

print("""
##############################
### CSyn Port Checker v1.1 ###
##############################
1.Default Settings
\ta.One SYN Packet Send Every Scan
If you want to exit press  Ctrl+C
If you don't want see verbose, change the verbose value with False
""")
time.sleep(1)

if len(sys.argv) != 4:
    print("usege: ./cportchecker.py <TargetIP> <Target Port> <Source Port>\n")
    sys.exit()

targe = sys.argv[1]
d_port = int(sys.argv[2])
s_port = int(sys.argv[3])

print("Checking is started..!")
time.sleep(0.6)

def portchecker():
    ip = IP(dst=targe)
    tcp = TCP(sport = s_port,dport=d_port, flags='S')
    ressponse = sr1((ip/tcp),timeout=3)
    flag_type = ressponse[TCP].flags
    if flag_type == 'SA':
        print(f"{d_port} is open!")
    elif flag_type == 'RA':
        print(f"{d_port} is open!")
    else:
        print(f"{d_port} is filtered or close!!")


portchecker()
