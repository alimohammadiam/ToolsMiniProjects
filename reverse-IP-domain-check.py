import requests
import json

data = {"remoteAddress": 'sabzlearn.ir'} 

http = requests.post("https://domains.yougetsignal.com/domains.php", data=data)

print(http)
