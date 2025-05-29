import requests, json, smtplib
from email.mime.text import MIMEText
from time import sleep

CONFIG = json.load(open("config.json"))

API_URL = 'https://www.tesla.com/coinorder/api/v4/inventory-results?query=' + json.dumps({
    "query": {
        "model": "my",
        "condition": "new",
        "options": {},
        "arrangeby": "Price",
        "order": "asc",
        "market": "TR",
        "language": "tr",
        "super_region": "north america",
        "lng": "",
        "lat": "",
        "zip": "",
        "range": 0
    },
    "offset": 0,
    "count": 24,
    "outsideOffset": 0,
    "outsideSearch": False,
    "isFalconDeliverySelectionEnabled": True,
    "version": "v2"
})

def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = CONFIG["email"]["from"]
    msg["To"] = CONFIG["email"]["to"]

    with smtplib.SMTP_SSL(CONFIG["email"]["smtp"], CONFIG["email"]["port"]) as server:
        server.login(CONFIG["email"]["from"], CONFIG["email"]["password"])
        server.send_message(msg)
        print("[+] Email sent.")

def check_inventory():
    try:
        r = requests.get(API_URL, headers={"User-Agent": "Mozilla/5.0"})
        data = r.json()
        results = data.get("results", [])
        if results:
            car = results[0]
            send_email("🚗 Tesla Model Y found in TR", f"First Match:\n{json.dumps(car, indent=2)}")
        else:
            print("[-] No inventory found.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    while True:
        check_inventory()
        sleep(CONFIG["interval_seconds"])
