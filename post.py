#!/usr/bin/python3
import requests
import json
headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic Y3J1YWRtaW46Y3J1YWRtaW4='}
load = {
"action":"action:closeReview",
"ignoreWarnings":"ignoreWarnings==true"
}
uri = "http://tiger.in.alcatel-lucent.com:8060/rest-service/reviews-v1/AMS9590-798/transition?action=action:closeReview"
response = requests.post(uri, data=load, headers=headers)
data=response.json()
print(data)
