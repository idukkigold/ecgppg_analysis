import heartbeat as hb
import numpy as np
import matplotlib.pyplot as plt

rfile =open("5-gamers/gamer1-ppg-2000-01-01.csv",'r')
ppg=[]
for line in rfile:
    line=line.split(',')
    ppg.append(line[1].strip("\n"))
    # print(line)



plt.plot(ppg)
plt.show()

# hr= hb.get_data(ppg)

# print(hr)