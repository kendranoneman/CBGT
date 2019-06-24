import numpy as np
import re
import os

cwd = os.getcwd()
path = cwd + '/net_example/network.pro'

all_info = []

with open (path, 'rt') as myFile:
    for myLine in myFile:
        all_info.append(myLine.rstrip('\n'))

#Retrieve event times
count = 0
eventTimes = []
eventID = []
sub1 = "EventTime"
for txt in all_info:
    if sub1 in txt:
        count+=1
        eventID.append(count)
        eventTimes.append([int(s) for s in txt.split() if s.isdigit()])
print(eventTimes)
print(eventID)

labels = []
sub2 = "Label"
for txt2 in all_info:
    if sub2 in txt2:
        labels.append(txt2.split("=",1)[1])

print(labels)
