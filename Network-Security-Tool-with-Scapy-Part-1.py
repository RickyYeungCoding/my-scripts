from scapy.all import *

def scan_port(target_ip, port):
    src_port = RandShort()
    response = sr1(IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
    if response is None:
        print(f"Port {port}: Filtered")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            print(f"Port {port}: Open")
            send(IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags="R"), verbose=0)
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Port {port}: Closed")

if __name__ == "__main__":
    target_ip = "192.168.0.146"
    ports_to_scan = range(1, 100)
    for port in ports_to_scan:
        scan_port(target_ip, port)
