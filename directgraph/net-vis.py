import numpy as np
import re

all_info = []

with open ('/Users/kendranoneman/Projects/coax/CBGT/autotest0/network.pro', 'rt') as myFile:
    for myLine in myFile:
        all_info.append(myLine.rstrip('\n'))

#Retrieve event times
eventTimes = []
sub1 = "EventTime"
for txt in all_info:
    if sub1 in txt:
        eventTimes.append([int(s) for s in txt.split() if s.isdigit()])
print(eventTimes)

labels = []
sub2 = "Label"
for txt2 in all_info:
    if sub2 in txt2:
        labels.append(txt2.split("=",1)[1])

print(labels)
