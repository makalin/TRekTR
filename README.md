# TRekTR

🚗🇹🇷 Tesla Model Y Inventory Tracker for Türkiye (TR)

**TRekTR** is a lightweight open-source bot that monitors Tesla's official inventory API for new Model Y listings in Türkiye (TR). When new vehicles are found, it automatically sends you an email alert.

## 📦 Features

- Checks Tesla's inventory API for Model Y (TR market)
- Sends email alerts if any new listings are found
- Configurable check interval
- Easy to run and customize

## 🔧 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/makalin/TRekTR.git
   cd TRekTR
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your settings**
   Edit `config.json` with your own SMTP email credentials:

   ```json
   {
     "email": {
       "from": "youremail@gmail.com",
       "to": "targetemail@gmail.com",
       "smtp": "smtp.gmail.com",
       "port": 465,
       "password": "your-app-password"
     },
     "interval_seconds": 3600
   }
   ```

   > 💡 *Use an [App Password](https://support.google.com/accounts/answer/185833) if you're using Gmail.*

4. **Run the tracker**

   ```bash
   python tracker.py
   ```

## 🛠 Planned Features

* Discord or Telegram webhook notifications
* Docker support
* Log history of found inventory
* Web dashboard UI (optional)

## 📜 License

MIT License. Contributions welcome.

---

Built for EV enthusiasts and car buyers in 🇹🇷 Türkiye (TR).
