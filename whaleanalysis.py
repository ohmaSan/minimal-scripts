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
    print(f"Whale buy count: {sell}")
else:
    print(f"Whale sell count: {buy}" )


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

timem = time.strftime('%X %x')


sell = int(firstBalance) - int(lastBalance)
buy = int(lastBalance) - int(lastBalance)

if firstBalance > lastBalance:
    print(f"While sell count: {sell}")
    with open("/home/x/Desktop/berry/hunt/signalling.txt","a") as f:
        f.write(f"{timem} ==> Whale buy count: {sell} \n")
else:
    print(f"{timem} ==> Whale buy count: {buy}")
    with open("/home/x/Desktop/berry/hunt/signalling.txt","a") as f:
        f.write(f"While buy cout: {buy} \n")

"""
