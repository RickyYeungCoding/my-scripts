import subprocess
import time

# Function to check if a host is reachable
def check_host(host):
    response = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if response.returncode == 0
    return True

# Main function
def main():
    host = "192.168.0.139"  # IP address to ping

    while True:
        if check_host(host):
            print("Network Active")
        else:
            print("Network Inactive")
        
        time.sleep(2)  # Wait for 2 seconds before next check

if __name__ == "__main__":
    main()
