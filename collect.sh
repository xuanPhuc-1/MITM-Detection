#!/bin/bash
for i in {1..2000}
do
    echo "Collecting data turn $i"
    # extract essential data from raw data
    sudo ovs-ofctl -O OpenFlow13 dump-flows s1 > data/raw.txt
    grep "nw_src" data/raw.txt > data/flowentries.csv
    grep "arp_op=1" data/raw.txt > ARP_data/ARP_Request_flowentries.csv
    grep "arp_op=2" data/raw.txt > ARP_data/ARP_Reply_flowentries.csv
    #packets=$(awk -F "," '{split($4,a,"="); print a[2]","}' data/flowentries.csv) 
    #bytes=$(awk -F "," '{split($5,b,"="); print b[2]","}' data/flowentries.csv)
    ipsrc=$(awk -F "," '{split($14,c,"="); print c[2]","}' data/flowentries.csv)    #14 cho l3
    ipdst=$(awk -F "," '{split($15,d,"="); print d[2]","}' data/flowentries.csv)    #15 cho l3
    ethsrc=$(awk -F "," '{split($12,e,"="); print e[2]","}' data/flowentries.csv)   #10 cho l2
    ethdst=$(awk -F "," '{split($13,f,"="); print f[2]","}' data/flowentries.csv)   #11 cho l2

    eth_src_reply=$(awk -F "," '{split($12,e,"="); print e[2]","}' ARP_data/ARP_Reply_flowentries.csv)   #10 cho l2
    ip_dst_reply=$(awk -F "," '{split($15,d,"="); print d[2]","}' ARP_data/ARP_Reply_flowentries.csv)    #15 cho l3


    if test -z "$ipsrc" || test -z "$ipdst" || test -z "$ethsrc" || test -z "$ethdst";
    then
        state=0
    else
        echo "$ipsrc" > data/ipsrc.csv
        echo "$ipdst" > data/ipdst.csv
        echo "$ethsrc" > data/ethsrc.csv
        echo "$ethdst" > data/ethdst.csv
        echo "$eth_src_reply" > ARP_data/eth_src_reply.csv
        echo "$ip_dst_reply" > ARP_data/ip_dst_reply.csv
    fi
    python3.8 computeTuples.py

    sleep 5
done


