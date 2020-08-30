import requests
import sys
import time

BASE="http://api.binance.com"
SECRET="ahljeb65Y5uxbyoQcexdZtdhcXdDBUUZHZAcww0GMbm9SmQ0L6WoVjf1xRV7vHjD"
API="W7xrWkVTfY0QdvpfwNhrkIOxSsqAzb2y6C1QchUvxleSDuglYABauqIuriLsxQYI"


def getTime():
    r=requests.get(BASE+"/api/v1/time")
    print(r.url)
    print(r.text)
    return r.text

def getTradeLis():
    payload={'symbol': 'ONTBTC', 'limit': '100' }
    r=requests.get(BASE+"/api/v1/trades", params=payload)
    print(r.url)
    print(r.text)
    return r.text

def getTradeDep():
    payload={'symbol': 'ONTBTC', 'limit': '100' }
    r=requests.get(BASE+"/api/v1/depth", params=payload)
    print(r.url)
    print(r.text)
    return r.text

def main(argv):
    getTime()
    time.sleep(1)
    getTradeLis()
    time.sleep(1)
    getTradeDep()


if __name__=='__main__':
    main(sys.argv)

