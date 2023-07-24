from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import RemoteController
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from multiprocessing import Process
import ipmininet
from ipmininet.cli import IPCLI
from ipmininet.ipnet import IPNet
from ipmininet.router.config import RouterConfig
from ipmininet.iptopo import IPTopo
from ipmininet.router.config.base import RouterConfig

def createTopology():
    #create custom topology can access to internet
    net = IPNet(topo=None)
    #add controller
    net.addController("c0", controller=RemoteController, ip="127.0.0.1", port=6633)
    #add one openvswitch
    s1 = net.addSwitch("s1", cls=OVSKernelSwitch)
    #add one router
    r1 = net.addRouter("r1", lo_addresses=["2042:1::1/64", "10.1.0.1/24"])
    #add one host
    h1 = net.addHost("h1", ip="10.1.0.2")
    
    #add link between switch and router
    ls1r1 = net.addLink(s1, r1)
    lh1s1 = net.addLink(h1,s1)
    ls1r1[r1].addParams(ip=("2042:12::1/64", "10.12.0.1/24"))
    ls1r1[s1].addParams(ip=("2042:12::2/64", "10.12.0.2/24"))
    
    lh1s1[r1].addParams(ip=("2042:1a::1/64", "10.13.0.1/24"))
    lh1s1[h1].addParams(ip=("2042:1a::2/64", "10.13.0.2/24"))
    
    #build topology
    net.build()
    for controller in net.controllers:
        controller.start()
    
    net.get("s1").start([controller])
    
    #start router
    r1.cmd("sysctl -w net.ipv6.conf.all.forwarding=1")
    r1.cmd("sysctl -w net.ipv4.ip_forward=1")
    r1.cmd("ip -6 route add 2042:1::/64 via 2042:12::2")
    
    
    
net = IPNet(topo=createTopology(), allocate_IPs=False)  # Disable IP auto-allocation
try:
    net.start()
    IPCLI(net)
finally:
    net.stop()