import numpy as np
import csv
import pandas as pd
import time
import os

HOME = os.path.expanduser('~')
time_interval = 1


with open('ARP_data/ARP_Reply_flowentries.csv', newline='') as f:
    reader = csv.reader(f)
    ARP_Reply = list(reader)
# count the number of ARP_Reply
ARP_Reply = len(ARP_Reply)
with open('ARP_data/ARP_Request_flowentries.csv', newline='') as f1:
    reader = csv.reader(f1)
    ARP_Request = list(reader)
# #check if the path /home/xuanphuc/MITM-Detection/ARP_Broadcast/arp_broadcast.csv exists do the following or not the a

path = HOME + '/MITM-Detection/ARP_Broadcast/arp_broadcast.csv'
with open(path, newline='') as f2:
    reader = csv.reader(f2)
    # format of arp_broadcast.csv: source Mac, time stamp
    arp_broadcast = list(reader)


arp_broadcast = len(arp_broadcast)
abps = arp_broadcast / time_interval

# count the number of ARP_Request
ARP_Request = len(ARP_Request)
ARP = ARP_Reply + ARP_Request

f.close()
f1.close()
f2.close()

aps = ARP / time_interval
subARP = ARP_Reply - ARP_Request

with open('f1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader = list(reader)

if int(reader[-1][-1]) > 0:
    if subARP >= 1:
        miss_match = 1
    else:
        miss_match = 0
else:
    miss_match = 0
# time stamp with minute:second format
time_stamp = time.strftime("%H:%M:%S", time.localtime())
# APS: ARP per second, ABPS: ARP broadcast per second, SUBARP: ARP reply - ARP request, MISS_MAC: miss match
headers = ["APS", "ABPS", "SUBARP", "MISS_MAC"]


# features_value = [aps, abps, subARP, miss_match, time_stamp]

features_value = [aps, abps, subARP, miss_match]
# print(dict(zip(headers, features)))
# print(features)

# with open('features-file.csv', 'a') as f:      #comment de test model
#     cursor = csv.writer(f, delimiter=",")
#     cursor.writerow(features)

# write the header to the first row of the csv file

with open('test.csv', 'a') as f:  # comment de test model
    cursor = csv.writer(f, delimiter=",")
    cursor.writerow(features_value)

with open('realtime.csv', 'w') as f:
    cursor = csv.writer(f, delimiter=",")
    cursor.writerow(headers)
    cursor.writerow(features_value)
    f.close()

# with open('dataset.csv', 'a') as f:            #comment de test model
#     cursor = csv.writer(f, delimiter=",")
#     cursor.writerow(headers)
#     cursor.writerow(features)
#     f.close()

# with open('evaluation.csv', 'a') as f:      #comment de test model
#     cursor = csv.writer(f, delimiter=",")
#     cursor.writerow(features)
