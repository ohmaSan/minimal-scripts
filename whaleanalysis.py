#whale analyzer, just 1 whale

with open("stalking.txt") as f:
        firstline = f.readlines()[1:2]
        wallet = firstline[0][24:64]
        fbalance = firstline[0][106:131]
        firstBalance = "".join(fbalance[0:7])
        intBalance = int(firstBalance)


with open("stalking.txt") as f:
        for line in f:
            pass
        last_line = line
        lbalance = last_line[106:131]
        lastBalance = "".join(lbalance[0:7])

sell = int(firstBalance) - int(lastBalance)
buy = int(lastBalance) - int(lastBalance)

if firstBalance > lastBalance:
    print(f"Whale buy count: {buy}")
else:
    print(f"Whale sell count: {sell}" )


"""

import time
#whale analyzer


with open("stalking.txt") as f:
        firstline = f.readlines()[1:2]
        wallet = firstline[0][24:64]
        fbalance = firstline[0][106:131]
        firstBalance = "".join(fbalance[0:7])
        intBalance = int(firstBalance)


with open("stalking.txt") as f:
        for line in f:
            pass
        last_line = line
        lbalance = last_line[106:131]
        lastBalance = "".join(lbalance[0:7])

sell = int(firstBalance) - int(lastBalance)
buy = int(lastBalance) - int(lastBalance)


timem = time.strftime('%X %x')
if firstBalance > lastBalance:
    print(f"While buy count: {sell}")
    with open("/home/x/Desktop/berry/hunt/signalling.txt","a") as f:
        f.write(f"While buy coint: {sell}" + f"First time:  {timem}")
else:
    print(f"While sell count: {buy}" + f"First time:  {timem}")
    with open("/home/x/Desktop/berry/hunt/signalling.txt","a") as f:
        f.write(f"While sell cout: {buy}")






"""
