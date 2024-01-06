## MITM-Detection

# Installation

## Run on Ubuntu 18.04:

```bash
pip install -r requirements.txt
```

## Run on Fedora:

### Step 1: Install python3.8

```bash
sudo dnf install python3.8
```

### Step 2: Install pip3 (use get-pip.py)

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.8 get-pip.py
```

### Step 3: Install dependencies

```bash
sudo python3.8 -m pip install -r requirements.txt
```

## Add line to the init file

```bash
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
```

### Step 1: run file l2_learning_mod.py on /pox/pox/forwarding/

```bash
python3.8 pox.py forwarding.l2_learning_new
```

### Step 2: Collect data

```bash
source collect.sh
```

### Step 3: Run controller (The traffic will generate automatically)

```bash
    sudo python3.8 ./custom_topo.py
```

### attack example h1 (attacker) -> h3, h7 (victim)

```bash
    ettercap -T -i h1-eth0 -M ARP /10.0.0.3// /10.0.0.7//
```
