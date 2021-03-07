import requests
import time

print("bscscanWalletStalker v1.1")

bscscan = "https://api.bscscan.com"
token = "0xf859Bf77cBe8699013d6Dbc7C2b926Aaf307F830"
api_key = "YOUR API KEY"

key = 0
print("First time:" + time.strftime('%X %x'))

with open("whales.txt") as f:
    print("Program is running! stalking.txt is creating..!\n")

    for wallets in f:
        r = requests.get(
            f'{bscscan}/api?module=account&action=tokenbalance&contractaddress={token}&address={wallets.strip()}&tag=latest&apikey={api_key}')
        print(time.strftime('%X %x ==> ') + wallets.strip() + " = " + r.text.strip())
        with open("stalking.txt", "a") as f:
            f.write(time.strftime('%X %x ==> ') + wallets.strip() + " = " + r.text.strip() + "\n")
        key += 1
        if key == 5:
            time.sleep(1)
            key = 0
