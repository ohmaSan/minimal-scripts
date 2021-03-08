import requests
import time

print("bscscanWalletStalker v1.1")

bscscan = "https://api.bscscan.com"
token = "0xf859Bf77cBe8699013d6Dbc7C2b926Aaf307F830"
api_key = "5YFEM1PDQW6QA5YY9FK9J9Z9WEP671SB95"

key = 0
print("First time:" + time.strftime('%X %x'))

while True:
    with open("whales.txt") as f:
        print("\nProgram is running! stalking.txt is creating..!")
        for wallets in f:
            r = requests.get(
                f'{bscscan}/api?module=account&action=tokenbalance&contractaddress={token}&address={wallets.strip()}&tag=latest&apikey={api_key}')
            print(time.strftime('%X %x ==> ') + wallets.strip() + " = " + r.text.strip())
            with open("stalking.txt", "a") as f:
                f.write("\n" + time.strftime('%X %x ==> ') + wallets.strip() + " = " + r.text.strip())
            key += 1
            if key == 3:
                with open("stalking.txt", "a") as f:
                    f.write("\n")
                time.sleep(1)
                key = 0
