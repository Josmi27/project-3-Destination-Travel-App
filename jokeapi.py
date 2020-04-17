import requests
import json


import requests

url = "https://joke3.p.rapidapi.com/v1/joke"

headers = {
    'x-rapidapi-host': "joke3.p.rapidapi.com",
    'x-rapidapi-key': "e9030cc69cmsh46998fa37a68441p18e133jsne5b9847bff25"
    }

response = requests.request("GET", url, headers=headers)

json_body = response.json()
rand_joke = json.dumps(json_body["content"], indent=2)



