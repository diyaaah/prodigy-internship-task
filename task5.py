import scapy.all as scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        payload = packet[scapy.Raw].load if scapy.Raw in packet else None
        
        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {protocol}, Payload: {payload}")

def start_sniffing(interface):
    scapy.sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == "__main__":
    interface = input("Enter the interface to sniff (e.g., eth0, wlan0): ")
    start_sniffing(interface)
