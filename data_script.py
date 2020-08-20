import os
import json
import requests

if not os.path.exists('data'):
    os.mkdir('data')

req = requests.get("https://api.covid19api.com/")

def base():
    """
    Gets the data from the base url
    """
    data = {}
    req = requests.get(base_url)
    if req.status_code==200:
        data = (json.loads(req.text)) #converts dict to text

    return data

def get_day_one():
    """
    Gets the data for day one by country
    """

    url = "{}dayone/country/{}/status/confirmed".format(base_url, country)
    data = {}
    req = requests.get(url)

    if req.status_code==200:
        data = (json.loads(req.text))

if __name__ == "__main__":
    print (get_day_one("canada"))
