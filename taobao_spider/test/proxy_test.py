import requests

try:
    requests.get('http://wenshu.court.gov.cn/', proxies={"https":"http://114.113.126.87:80"}, timeout=5)
    # requests.get('http://wenshu.court.gov.cn/', proxies={"http":"http://113.12.72.24:3128"}, timeout=5)
except:
    print ('connect failed')
else:
    print ('success')