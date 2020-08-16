import os
import sys
import json
import requests
os.system("clear")
os.system("figlet -f standard Public IP")
print
print "Author :  Rahat Khan Tusar(RKT)"
print
url = "https://httpbin.org/ip"
resp = requests.get(url)
print (resp.json)
print (resp.text)



