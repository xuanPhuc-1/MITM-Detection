import numpy as np
import csv
import pandas as pd
import time
time_interval = 3


with open('ARP_data/ARP_Reply_flowentries.csv', newline='') as f:
    reader = csv.reader(f)
    ARP_Reply = list(reader)
#count the number of ARP_Reply
ARP_Reply = len(ARP_Reply)
with open('ARP_data/ARP_Request_flowentries.csv', newline='') as f1:
    reader = csv.reader(f1)
    ARP_Request = list(reader)
# #check if the path /home/xuanphuc/MITM-Detection/ARP_Broadcast/arp_broadcast.csv exists do the following or not the a
with open('/home/xuanphuc/MITM-Detection/ARP_Broadcast/arp_broadcast.csv', newline='') as f2:
    reader = csv.reader(f2)
    #format of arp_broadcast.csv: source Mac, time stamp
    arp_broadcast = list(reader)

arp_broadcast = len(arp_broadcast)
abps = arp_broadcast / time_interval

#count the number of ARP_Request
ARP_Request = len(ARP_Request)
ARP = ARP_Reply + ARP_Request
f.close()
f1.close()
f2.close()

aps = ARP / time_interval              
subARP = ARP_Reply - ARP_Request         
#time stamp with minute:second format
time_stamp = time.strftime("%M:%S", time.localtime())
headers = ["APS", "ABPS", "SUBARP", "time_stamp"]

features = [aps, abps, subARP, time_stamp]

# print(dict(zip(headers, features)))
# print(features)

with open('features-file.csv', 'a') as f:
    cursor = csv.writer(f, delimiter=",")
    cursor.writerow(features)


with open('realtime.csv', 'w') as f:
    cursor = csv.writer(f, delimiter=",")
    cursor.writerow(headers)
    cursor.writerow(features)
    
    f.close()