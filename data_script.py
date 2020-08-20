import os
import json
import requests

if not os.path.exists('data'):
    os.mkdir('data')

req = requests.get("https://api.covid19api.com/")

if req.status_code==200:
    data = (json.loads(req.text)) #converts dict to text
    print (data.keys())
