from datetime import datetime
from OpenSSL import crypto
import telegram
import asyncio

# check expiry of tls.cert for lnbits. if expired it stoppes working

# Telegram Bot API token
TOKEN = 'FILL IN YOUR OWN TOKEN'

# Telegram chat ID to send the notifications to
CHAT_ID = 'FILL IN YOUR OWN ID'


def check_cert_expiry(cert_path):
    with open(cert_path, 'rb') as f:
        cert_data = f.read()
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_data)
        expiry_date = datetime.strptime(cert.get_notAfter().decode('ascii'), "%Y%m%d%H%M%SZ")
        return expiry_date

def main():
    cert_path = '/PATH TO YOUR/tls.cert'  # Replace with the actual path to your TLS certificate
    expiry_date = check_cert_expiry(cert_path)
    current_date = datetime.utcnow()

    #print("TLS Certificate Expiry Date:", expiry_date)

    if current_date > expiry_date:
        message = f"⚠️ Certificate has expired: {expiry_date} ⚠️"
        # print(message)
    else:
        days_until_expiry = (expiry_date - current_date).days
        if days_until_expiry < 30:
           message = f"⚠️ TLS.cert is about to expire in {days_until_expiry} on {expiry_date} ⚠️"
           # print(message)

    async def send_telegram_notification():
        # Send the notification to Telegram
        bot = telegram.Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=message)

    # Execute the send_telegram_notification coroutine using asyncio.run()
    asyncio.run(send_telegram_notification())

if __name__ == "__main__":
    main()
