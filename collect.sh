#!/bin/bash
for i in {1..2000}
do
    echo "Collecting data turn $i"
    # extract essential data from raw data
    sudo ovs-ofctl -O OpenFlow13 dump-flows s1 > data/raw.txt
    grep "nw_src" data/raw.txt > data/flowentries.csv
    grep "arp_op=1" data/raw.txt >> ARP_data/ARP_Request_flowentries.csv
    grep "arp_op=2" data/raw.txt >> ARP_data/ARP_Reply_flowentries.csv
    #packets=$(awk -F "," '{split($4,a,"="); print a[2]","}' data/flowentries.csv) 
    #bytes=$(awk -F "," '{split($5,b,"="); print b[2]","}' data/flowentries.csv)
    ipsrc=$(awk -F "," '{split($14,c,"="); print c[2]","}' data/flowentries.csv)    #14 cho l3
    ipdst=$(awk -F "," '{split($15,d,"="); print d[2]","}' data/flowentries.csv)    #15 cho l3
    ethsrc=$(awk -F "," '{split($12,e,"="); print e[2]","}' data/flowentries.csv)   #10 cho l2
    ethdst=$(awk -F "," '{split($13,f,"="); print f[2]","}' data/flowentries.csv)   #11 cho l2

    
    # ipsrc=$(awk -F "," '{out=""; for(k=2;k<=NF;k++){out=out" "$k}; print out}' data/flowentries.csv | awk -F " " '{split($15,d,"="); print d[2]","}')
    # ipdst=$(awk -F "," '{out=""; for(k=2;k<=NF;k++){out=out" "$k}; print out}' data/flowentries.csv | awk -F " " '{split($16,d,"="); print d[2]","}')
    # inport=$(awk -F "," '{out=""; for(k=2;k<=NF;k++){out=out" "$k}; print out}' data/flowentries.csv | awk -F " " '{split($10,d,"="); print d[2]","}')
    # check if there are no traffics in the network at the moment.
    if test -z "$ipsrc" || test -z "$ipdst" || test -z "$ethsrc" || test -z "$ethdst";
    then
        state=0
    else
        echo "$ipsrc" > data/ipsrc.csv
        echo "$ipdst" > data/ipdst.csv
        echo "$ethsrc" > data/ethsrc.csv
        echo "$ethdst" > data/ethdst.csv
    fi


    sleep 3
done


