from scapy.all import *

def detect_stealth_scan(packet):
    if packet.haslayer(TCP) and packet[TCP].flags == 2:  # Check if the TCP flag is SYN (2)
        print(f"Possible TCP SYN Stealth Scan detected from {packet[IP].src}")

if __name__ == "__main__":
    sniff(filter="tcp", prn=detect_stealth_scan)
