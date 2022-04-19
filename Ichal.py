import requests
import time

# logo
print ('-----------------------------------------------')
print ('[+] Creator : Ichal Sendana')
print ('[+] YouTube : Ichal sendana')
print ('-----------------------------------------------')
print ('\n[+] Nomor Di Awali 8xxxxx')

# Run nomor
nomor = input('[+] Nomor Terget : ')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'terkirim' in req:
      print ('[√] spam terkirim')
else:
      print ('[!] spam gagal')
