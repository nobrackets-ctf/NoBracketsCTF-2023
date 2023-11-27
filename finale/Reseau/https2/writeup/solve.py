import requests
import re
from time import sleep

with open("serials.txt") as f:
    serials = f.readlines()

for serial in serials:
    sleep(1)
    url = "https://crt.sh/?serial="+serial.strip()
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"}).text
    matches = re.findall(r'<TD style="text-align:center"><A href="\?id=(\d+)">\d+</A></TD>', r)
    if len(matches) == 0:
        print("no match for", serial.strip())
    for match in matches:
        sleep(1)
        url = "https://crt.sh/?id="+match
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"}).text
        data = r[r.find("Subject:"):r.find('Subject:')+1000].replace("&nbsp;", "")
        print(data.split("<BR>")[1])

