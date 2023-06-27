# MITM-Detection
# Test Traffic
# Step 1: run file l2_learning_mod.py on /pox/pox/forwarding
python3 pox.py forwarding.l2_learning_mod 
# Step 2: Collect data
source collect.sh
# Step 3: Run controller (The traffic will generate automatically)
sudo python3 ./custom_topo.py 



# add line

arp_request_count = 0
arp_reply_count = 0
arp_request_previous_count = 0
arp_reply_previous_count = 0
arp_request_rate = 0
arp_reply_rate = 0
arp_total=0
delta_arp=0
time_interval=1.0
mismatch_mac_ip_count=0