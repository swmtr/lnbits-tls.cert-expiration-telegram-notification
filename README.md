# tls.cert Expiration Notification to Telegram

Sometimes when connecting services such as LNbits to your own local node with LndRestWallet, you forget that the tls.cert you use has an expiry date. When the tls.cert certificate expires your connection to LNbits stops working and you then are left wondering why when paying lightning invoices, your backend will be unreachable. In term sof LNbits, the wallet automatically defaults to the VoidWallet which is of course not functional. You could also see some services on your node having the following issues: Failed to connect with gRPC to remote LND

You can check the expiry date of your tls.cert by running this command:

```
openssl x509 -in /path/to/tls.cert -noout -dates
```

## Pre-requsites

I already assume, your Linux setup has python installed and you can execute python scripts.

Also, you should already have Telegram bot data - if not, check -> https://github.com/swmtr/LNbits-payment-notifications-to-telegram?tab=readme-ov-file#telegram-bot

1. pyOpenSSL installed

We will use the pyOpenSSL python package to check the certtificate validity. Run the following command:

```
sudo pip install pyOpenSSL
```

2. Python Telegram library

Your script will need to communicate with Telegram. To get the library, run this command:
```
pip install python-telegram-bot
```

## The script

Grab the Python script and modify your Telegram data in it, the path to the tls.cert, and what your threshold is for notification.


## Automating the notifications
  
When the script notifies you correctly of the tls.cert script being close to expiry, run the following command to open your crontab.

```
crontab -e
```

Add the following into it.

```
# run check every first day of the month at midnight to see if tls.cert on lnbits is expired
0 0 1 * * /usr/bin/python3 /ABSOLUTE PATH TO YOUR PYTHON FILE/lnbits-tls-check.py >> /ABSOLUTE PATH TO YOUR CRONLOG FILE 2>&1
```

# End Notes

This setup is just a hack to get notified. It is by no means perfect, but it will do the job.

If you found this guide useful, why not let it be known by [sending me a few sats](https://360swim.com/ln-donate-github) or via LN address⚡swmtr@360swim.com .
<br />
<img src="https://360swim.com/user/themes/swimquark/images/ln_git.png" width="400" />

Finally, if you are into swimming, checkout some [swimming tips](https://360swim.com/tips).
