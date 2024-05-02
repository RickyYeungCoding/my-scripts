import smtplib
import socket
from email.mime.text import MIMEText
from datetime import datetime
import time

def send_email(sender_email, sender_password, recipient_email, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message)
    server.quit()

def check_host_status(host):
    try:
        socket.create_connection((host, 80), timeout=5)
        return "up"
    except:
        return "down"

def main():
    sender_email = input("rickaye07@gmail.com: ")
    sender_password = input("Password: ")
    recipient_email = input("Yeungho455@gmail.com: ")

    hosts = {"google.com": "up"}

    while True:
        for host, status in hosts.items():
            current_status = check_host_status(host)

            if current_status != status:
                message = f"Host {host} status changed from {status} to {current_status} at {datetime.now()}."
                send_email(sender_email, sender_password, recipient_email, "Host Status Change", message)
                hosts[host] = current_status

        time.sleep(60)

if __name__ == "__main__":
    main()
