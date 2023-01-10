import requests
import time

while True:
    req = requests.get('https://www.facebook.com/')
    print(req.status_code)
    if req.status_code != 200:
        #Inform the facebook
        pass
    time.sleep(5)
