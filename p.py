import heartbeat as hb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rfile =open("5-gamers/gamer1-ppg-2000-01-01.csv",'r')
ppg=[]
for i,line in enumerate(rfile):
    if i!=0:
        line=line.split(',')
        ppg.append(line[1].strip("\n"))

ppg=np.array([int(elem) for elem in ppg])

ppg=ppg[ppg>=100]



plt.plot(ppg[1:1000])
plt.show()

measures = hb.process(ppg[300:1100],100)

print(measures)

hb.plotter()


