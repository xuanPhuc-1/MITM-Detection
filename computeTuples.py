import numpy as np
import csv
import pandas as pd
# from scipy.stats import entropy



time_interval = 2


# Number of source IPs
# Speed of source IP (SSIP), number of source IPs per unit of time
# SSIP = Number of different IP sources / T period
with open('ARPdata/ARP_Reply_flowentries.csv', newline='') as f:
    reader = csv.reader(f)
    ARP_Reply = list(reader)
eth_src_reply
ip_dst_reply
# print(n_ip)
ssip = n_ip // time_interval               # Get number of IPs for every second by multiple interval - 4s
f.close()




# Number of Flow entries
# Speed of Flow entries (SFE), number of flow entries to the switch per unit of time
# SFE = Number of flow entries / T period
sfe = n_ip // 3

# Number of interactive flow entries

headers = ["SSIP", "SDFP", "SDFB", "SFE", "RFIP", "ENTROPY"]

features = [ssip, sdfp, sdfb, sfe, rfip, entropy.value]

# print(dict(zip(headers, features)))
# print(features)

with open('features-file.csv', 'a') as f:
    cursor = csv.writer(f, delimiter=",")
    #cursor.writerow(headers)
    cursor.writerow(features)


with open('realtime.csv', 'w') as f:
    cursor = csv.writer(f, delimiter=",")
    cursor.writerow(headers)
    cursor.writerow(features)
    
    f.close()