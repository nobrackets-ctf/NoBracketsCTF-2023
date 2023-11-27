Les paquets HTTP semblent ne pas contenir d'informations mais on voit aussi des paquets [OCSP](https://fr.wikipedia.org/wiki/Online_Certificate_Status_Protocol). Ce protocole permet de vérifier qu'un certificat est toujours valide auprès de l'émetteur dès qu'un site HTTPS est visité. La requête contient le numéro de série du certificat et un site tel que [crt.sh](https://crt.sh/) permet de chercher un certificat à partir de son numéro de série et retrouver le domaine du site.

On extrait tous les numéros de série en éliminant les doublons avec cette commande :

`tshark -r http.pcapng -T fields -e ocsp.serialNumber | sort | uniq > serials.txt`

On peut faire un script Python pour automatiser la recherche sur crt.sh mais il faudra faire attention à ne pas requêter trop vite au risque de se faire bannir du site. Exemple de script très sale type CTF :

```py
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
```


Liste des domaines extraites en quelques minutes :

```
commonName=*.googleusercontent.com
commonName=*.google.com
commonName=*.google.com
commonName=*.gstatic.com
commonName=upload.video.google.com
commonName=edgestatic.com
commonName=remote-settings.mozilla.org
commonName=remote-settings.mozilla.org
commonName=push.services.mozilla.com
commonName=push.services.mozilla.com
commonName=pochta.q0.ru
commonName=pochta.q0.ru
commonName=contile.services.mozilla.com
commonName=contile.services.mozilla.com
commonName=content-signature-2.cdn.mozilla.net
commonName=*.telemetry.mozilla.org
commonName=*.c.docs.google.com
commonName=www.google.com
```

Flag : `NBCT{pochta.q0.ru}`