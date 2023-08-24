import pyshark
import csv
import time
#create a array to store the packets
#using pyshark to capture all the packets in the network and store them in the array

packets = []
while True:
    #packets = []    
    #open file capture.csv
    #wipe data in the file
    #with open('capture.csv', 'w') as csvfile:
        #csvfile.write('')
    #capture packets
    capture = pyshark.LiveCapture(interface='Loopback')


    #capture 100 packets
    capture.sniff(packet_count=150)

    #store the packets in the array
    for packet in capture.sniff_continuously(packet_count=150):
        packets.append(packet)
    #Extract the the raw packet type from OpenFlow Packet_In in the Loopback interface
    for packet in packets:
        if packet.highest_layer == 'OPENFLOW_V1':
            print(packet.show())
                
    # #display the packets
    # for packet in packets:
    #     #if the packet is a ARP packet, print it
    #     if packet.highest_layer == 'ARP' and packet.arp.dst_hw_mac == '00:00:00:00:00:00':
    #         #print all the attributes of the packet
    #         with open('capture.csv', 'a') as csvfile:
    #             csvfile.write(str(packet.arp.src_hw_mac) + '\n') 
     
    #time.sleep(3)
            
        

