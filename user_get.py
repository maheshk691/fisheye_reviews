#!/usr/bin/python3
import requests
import json
def active_users_get():
	active_users = []
	headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic Y3J1YWRtaW46Y3J1YWRtaW4='}
	resp = requests.get('http://tiger.in.alcatel-lucent.com:8060/rest-service/users-v1',  headers=headers)
	data=resp.json()
	for i in data['userData']:
		active_users.append(i['userName'])
 
	print(active_users)
active_users_get()