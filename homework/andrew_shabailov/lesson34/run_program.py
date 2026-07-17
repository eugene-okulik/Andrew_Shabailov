from datetime import datetime
import requests
from time import sleep


while True:
    requests.get("http://google.com")
    print(datetime.now())
    sleep(1)
