import heartbeat as hb
import numpy as np
import matplotlib.pyplot as plt

rfile =open("5-gamers/gamer1-ppg-2000-01-01.csv",'r')
ppg=[]
for i,line in enumerate(rfile):
    if i!=0:
        line=line.split(',')
        ppg.append(line[1].strip("\n"))
        # print(line)



ppg=np.array([int(elem) for elem in ppg])

print(type(ppg[1]))


plt.plot(ppg)
plt.show()

measures = hb.process(ppg,100)

print(measures)