import time
import requests
import os

urls = ["https://www.lidl.de/c/online-prospekte/s10005610", 
        "https://www.lidl.pl/c/nasze-gazetki/s10008614",
        "https://www.lidl.bg/c/broshura/s10020060",
        "https://www.lidl.be/c/nl-BE/folders-magazines/s10008101",
        "https://www.lidl.sk/c/online-letak/s10008489",
        "https://www.lidl.nl/c/service-contact-folders/s10008124",
        "https://www.lidl.ro/c/cataloage-online/s10019911"]

filename = "output.txt"  
ok_response = 201
check_interval = 10

while True:
    for url in urls:
        response = requests.get(url)
        if response.status_code != ok_response:
            os.system(f"curl -s -I -D - {url} >> {filename}")
    time.sleep(check_interval) 