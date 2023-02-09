import socket
import requests

def get_ip(domain):
    return socket.gethostbyname(domain)

def send_to_telegram(ip, domain):
    bot_token = "your_telegram_bot_token"
    bot_chatID = "your_telegram_chat_id"
    send_text = f"The IP address for {domain} is: {ip}"
    send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&text={send_text}"
    requests.get(send_url)

# List of domains to check
domains = ["google.com", "facebook.com", "amazon.com"]

for domain in domains:
    try:
        ip = get_ip(domain)
        send_to_telegram(ip, domain)
        print(f"The IP address for {domain} is: {ip}")
    except socket.gaierror as e:
        print(f"Could not resolve hostname for {domain}: {e}")
