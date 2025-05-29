# TRekTR

🚗🇹🇷 Türkiye (TR) için Tesla Model Y Envanter Takipçisi

**TRekTR**, Tesla’nın resmi envanter API’sini kullanarak Türkiye (TR) pazarı için yeni Model Y ilanlarını takip eden hafif ve açık kaynaklı bir bottur. Yeni araçlar bulunduğunda otomatik olarak size e-posta bildirimi gönderir.

## 📦 Özellikler

- Tesla’nın envanter API’sini Model Y için (TR pazarı) kontrol eder
- Yeni ilanlar bulunduğunda e-posta bildirimi gönderir
- Kontrol sıklığı ayarlanabilir
- Kurulumu ve özelleştirmesi kolay

## 🔧 Kurulum Talimatları

1. **Projeyi klonlayın**
   ```bash
   git clone https://github.com/makalin/TRekTR.git
   cd TRekTR
````

2. **Bağımlılıkları yükleyin**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ayarları yapılandırın**
   `config.json` dosyasını kendi SMTP e-posta bilgilerinizle düzenleyin:

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

   > 💡 *Gmail kullanıyorsanız bir [Uygulama Şifresi](https://support.google.com/accounts/answer/185833) oluşturun.*

4. **Botu çalıştırın**

   ```bash
   python tracker.py
   ```

## 🛠 Planlanan Özellikler

* Discord veya Telegram üzerinden bildirim gönderme
* Docker desteği
* Bulunan araçların log kaydı
* Web paneli arayüzü (isteğe bağlı)

## 📜 Lisans

MIT Lisansı. Katkılar memnuniyetle karşılanır.

---

🇹🇷 Türkiye’deki elektrikli araç meraklıları ve alıcıları için geliştirilmiştir.
