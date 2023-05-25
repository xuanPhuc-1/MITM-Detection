import subprocess, sys #to handle the Ryu output
import signal #for timer
import os #for process handling
import numpy as np #for model features
import pickle #to use ML model real-time
import pandas as pd #to use ML model real-time

proj_location = "/home/xuanphuc/traffic_classifier_sdn/"
dataset_location = proj_location+"dataset/"
## command to run ##
cmd = "python3.8 pox.py forwarding.l2_learning_mod"
flows = {} #empty flow dictionary
TIMEOUT = 5*60 #15*60 #15 min #how long to collect training data
class Flow:
    def __init__(self, time_start, datapath, inport, ethsrc, ethdst, outport, packets, bytes):
        self.time_start = time_start
        self.datapath = datapath
        self.inport = inport
        self.ethsrc = ethsrc
        self.ethdst = ethdst
        self.outport = outport
        
        #attributes for forward flow direction (source -> destination)
        self.forward_packets = packets
        self.forward_bytes = bytes
        self.forward_delta_packets = 0
        self.forward_delta_bytes = 0
        self.forward_inst_pps = 0.00
        self.forward_avg_pps = 0.00
        self.forward_inst_bps = 0.00
        self.forward_avg_bps = 0.00
        self.forward_status = 'ACTIVE'
        self.forward_last_time = time_start
        
        #attributes for reverse flow direction (destination -> source)
        self.reverse_packets = 0
        self.reverse_bytes = 0
        self.reverse_delta_packets = 0
        self.reverse_delta_bytes = 0
        self.reverse_inst_pps = 0.00
        self.reverse_avg_pps = 0.00
        self.reverse_inst_bps = 0.00
        self.reverse_avg_bps = 0.00
        self.reverse_status = 'INACTIVE'
        self.reverse_last_time = time_start

        self.arp_reply = 0
        
    #updates the attributes in the forward flow direction
    def updateforward(self, packets, bytes, curr_time):
        self.forward_delta_packets = packets - self.forward_packets
        self.forward_packets = packets
        if curr_time != self.time_start: self.forward_avg_pps = packets/float(curr_time-self.time_start)
        if curr_time != self.forward_last_time: self.forward_inst_pps = self.forward_delta_packets/float(curr_time-self.forward_last_time)
        
        self.forward_delta_bytes = bytes - self.forward_bytes
        self.forward_bytes = bytes
        if curr_time != self.time_start: self.forward_avg_bps = bytes/float(curr_time-self.time_start)
        if curr_time != self.forward_last_time: self.forward_inst_bps = self.forward_delta_bytes/float(curr_time-self.forward_last_time)
        self.forward_last_time = curr_time
        
        if (self.forward_delta_bytes==0 or self.forward_delta_packets==0): #if the flow did not receive any packets of bytes
            self.forward_status = 'INACTIVE'
        else:
            self.forward_status = 'ACTIVE'

    #updates the attributes in the reverse flow direction
    def updatereverse(self, packets, bytes, curr_time):
        self.reverse_delta_packets = packets - self.reverse_packets
        self.reverse_packets = packets
        if curr_time != self.time_start: self.reverse_avg_pps = packets/float(curr_time-self.time_start)
        if curr_time != self.reverse_last_time: self.reverse_inst_pps = self.reverse_delta_packets/float(curr_time-self.reverse_last_time)
        
        self.reverse_delta_bytes = bytes - self.reverse_bytes
        self.reverse_bytes = bytes
        if curr_time != self.time_start: self.reverse_avg_bps = bytes/float(curr_time-self.time_start)
        if curr_time != self.reverse_last_time: self.reverse_inst_bps = self.reverse_delta_bytes/float(curr_time-self.reverse_last_time)
        self.reverse_last_time = curr_time

        if (self.reverse_delta_bytes==0 or self.reverse_delta_packets==0): #if the flow did not receive any packets of bytes
            self.reverse_status = 'INACTIVE'
        else:
            self.reverse_status = 'ACTIVE'


def printflows(traffic_type,f):
    for key,flow in flows.items():
        outstring = '\t'.join([
        str(flow.forward_packets),
        str(flow.forward_bytes),
        str(flow.forward_delta_packets),
        str(flow.forward_delta_bytes), 
        str(flow.forward_inst_pps), 
        str(flow.forward_avg_pps),
        str(flow.forward_inst_bps), 
        str(flow.forward_avg_bps), 
        str(flow.reverse_packets),
        str(flow.reverse_bytes),
        str(flow.reverse_delta_packets),
        str(flow.reverse_delta_bytes),
        str(flow.reverse_inst_pps),
        str(flow.reverse_avg_pps),
        str(flow.reverse_inst_bps),
        str(flow.reverse_avg_bps),
        str(traffic_type)])
        f.write(outstring+'\n')

def run_ryu(p,traffic_type=None,f=None,model=None):
    ## run it ##
    time = 0
    while True:
        #reading output of Ryu 'simple_monitor_AK.py' script
        out = p.stdout.readline()
        if out == '' and p.poll() != None:
            break
        #check the ouput of the Ryu script to see if it is a flow stats update
        if out != '' and out.startswith(b'Detect'): #when Ryu 'simple_monitor_AK.py' script returns output
            #print('Head\ttime\t\tdatapath\tin-port\teth_src\t\t\teth-dst\t\t\tout_port\ttotal_packet\ttotal_bytes')
            
            fields = out.split(b'\t')[1:] #split the flow details
            
            fields = [f.decode(encoding='utf-8', errors='strict') for f in fields] #decode flow details 
           #print("Head    time            datapath        in-port eth_src                 eth-dst                 out_port        total_packet    total_bytes")
           #print("      ",1654900961        1              2       00:00:00:00:00:02                       00:00:00:00:00:01                       1       167916          11082460
           
            
            #print("      ",fields[0],"\t",fields[1],"\t\t",fields[2],"\t",fields[3],"\t",fields[4],"\t",fields[5],"\t\t",fields[6],"\t",fields[7])                #Ahmed Abdulwhhab
            unique_id = hash(''.join([fields[1],fields[3],fields[4]])) #create unique ID for flow based on switch ID, source host,and destination host
            
            #print("unique_id is ",unique_id)                #Ahmed Abdulwhhab
            if unique_id in flows.keys():
                flows[unique_id].updateforward(int(fields[6]),int(fields[7]),int(fields[0])) #update forward attributes with time, packet, and byte count
            else:
                rev_unique_id = hash(''.join([fields[1],fields[4],fields[3]])) #switch source and destination to generate same hash for src/dst and dst/src
                if rev_unique_id in flows.keys():
                    flows[rev_unique_id].updatereverse(int(fields[6]),int(fields[7]),int(fields[0])) #update reverse attributes with time, packet, and byte count
                else:
                    flows[unique_id] = Flow(int(fields[0]), fields[1], fields[2], fields[3], fields[4], fields[5], int(fields[6]), int(fields[7])) #create new flow object
            if not model is None:
                if time%1==0: #print output of model every 10 seconds
                    print("You are using the model ", model)                    
            else:
                printflows(traffic_type,f) #for training data
        time += 1

if __name__ == '__main__':
    SUBCOMMANDS = ('train', 'unsupervised', 'supervised')
    if len(sys.argv) >= 2:
        if sys.argv[1] == "train":
            if len(sys.argv) == 3:
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) #start Ryu process
                traffic_type = sys.argv[2]
                f = open(dataset_location+traffic_type+'_training_data.csv', 'w') #open training data output file
                signal.alarm(TIMEOUT) #set for 15 minutes
                print("Collecting training data for %s traffic. Please wait..."%traffic_type)
                try:
                    headers = 'Forward Packets\tForward Bytes\tDelta Forward Packets\tDelta Forward Bytes\tForward Instantaneous Packets per Second\tForward Average Packets per second\tForward Instantaneous Bytes per Second\tForward Average Bytes per second\tReverse Packets\tReverse Bytes\tDelta Reverse Packets\tDelta Reverse Bytes\tDeltaReverse Instantaneous Packets per Second\tReverse Average Packets per second\tReverse Instantaneous Bytes per Second\tReverse Average Bytes per second\tTraffic Type\n'
                    f.write(headers)
                    run_ryu(p,traffic_type=traffic_type,f=f)
                except Exception:
                    print('Exiting')
                    os.killpg(os.getpgid(p.pid), signal.SIGTERM) #kill ryu process on exit
                    f.close()
            else:
                print("ERROR: specify traffic type.\n")
        else:
            
            #start Ryu process
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) #start ryu process
            if sys.argv[1] == 'supervised':
                infile = open('NN_Reg','rb') 
            elif sys.argv[1] == 'unsupervised':
                infile = open('KMeans_Clustering','rb')
            model = pickle.load(infile) #unload previously trained ML model (refer to Jupyter notebook for details)
            infile.close()
            run_ryu(p,model=model)
    sys.exit();