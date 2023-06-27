# MITM-Detection
# Test Traffic
# Step 1: run file l2_learning_mod.py on /pox/pox/forwarding
python3 pox.py forwarding.l2_learning_mod 
# Step 2: Collect data
source collect.sh
# Step 3: Run controller (The traffic will generate automatically)
sudo python3 ./custom_topo.py 
