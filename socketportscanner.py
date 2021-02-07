import socket
from IPy import IP


# Multiple targets and spesific port scanner

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def port_scan(targets, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((targets, port))
        print(f"{targets} is {port} Open!")
    except:
        print(f"{targets} is {port} Close!")


targets = input("Target/s: ")
port = int(input("Port: "))

if ',' in targets:
    for target in targets.split(','):
        port_scan(check_ip(target.strip()), port)
else:
    port_scan(targets, port)
