import time
import requests
import os
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s %(message)s')

filename = "output.txt"  
ok_response = 200
check_interval = 30

with open("urls.txt", "r") as file:
    urls = [line.strip() for line in file]

while True:
    for url in urls:
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            continue
        if response.status_code != ok_response:
            os.system(f"echo {url} >> {filename}")
            os.system(f"curl -s -I -L {url} >> {filename}")
    time.sleep(check_interval)