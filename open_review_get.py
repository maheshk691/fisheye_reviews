#!/usr/bin/python3
import requests
import json
def reviews_open_get():
	authors = []
	users = []
	#users = []
	headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic Y3J1YWRtaW46Y3J1YWRtaW4='}
	resp = requests.get('http://tiger.in.alcatel-lucent.com:8060/rest-service/reviews-v1/filter?states=Review,Summarize', headers=headers)
	data=resp.json()
	for i in data['reviewData']:
		authors = i['author']
			for key, value in authors.items():
				  if key == "userName":
						users.append(value)

          return users

def active_users_get():
	active_users = []
	headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic Y3J1YWRtaW46Y3J1YWRtaW4='}
	resp = requests.get('http://tiger.in.alcatel-lucent.com:8060/rest-service/users-v1',  headers=headers)
	data=resp.json()
	for i in data['userData']:
		active_users.append(i['userName'])
 
	return active_users

activeusers = active_users_get()
reviewusers = reviews_open_get()

inactive_user = (list(set(reviewusers).difference(set(activeusers))))
inactive_user.sort()
print(inactive_user)

for i in inactive_user:
   open_review_get(i)
   
def open_review_get(i):
	open_review = []
	i = user
	url = http://tiger.in.alcatel-lucent.com:8060/rest-service/reviews-v1/filter?creator=+user+&states=Review
	headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic Y3J1YWRtaW46Y3J1YWRtaW4='}
	resp = requests.get(url, headers=headers)
	data=resp.json()
	for i in data['userData']:
		open_review.append(i['permaId'])
 
	return open_review
