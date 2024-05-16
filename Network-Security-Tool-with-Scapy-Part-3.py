from scapy.all import sr1, IP, ICMP, TCP

def ping_host(ip):
    response = sr1(IP(dst=ip)/ICMP(), timeout=2, verbose=0)
    return response is not None

def scan_ports(ip):
    common_ports = [22, 23, 443]
    open_ports = []

    for port in common_ports:
        response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
        if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
            open_ports.append(port)
            sr1(IP(dst=ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)

    if open_ports:
        print(f"Open ports on {ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {ip}.")

def main():
    while True:
        ip = input("Enter an IP address to scan (or 'exit' to stop): ")
        if ip.lower() == 'exit':
            break
        if ping_host(ip):
            print(f"Host {ip} is successful.")
            scan_ports(ip)
        else:
            print(f"Host {ip} is not successful.")

if __name__ == "__main__":
    main()
