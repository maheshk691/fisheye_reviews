#!/usr/bin/python3
import requests
import json
def reviews_users_get():
	authors = []
	users = []
    #users = []
	headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic Y3J1YWRtaW46Y3J1YWRtaW4='}
	resp = requests.get('http://test.com/rest-service/reviews-v1/filter?states=Review,Summarize',  headers=headers)
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
	resp = requests.get('http://test.com/rest-service/users-v1',  headers=headers)
	data=resp.json()
	for i in data['userData']:
		active_users.append(i['userName'])
 
	return active_users

def open_review_get(inactive_user):
	permaId = []
	for i in inactive_user:
		url = "http://test.com/rest-service/reviews-v1/filter?creator="+i+"&author="+i+"&moderator="+i+"&reviewer="+i+"&states=Review"
		print("Open Review of the userName:",i)
		headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic Y3J1YWRtaW46Y3J1YWRtaW4='}
		resp = requests.get(url, headers=headers)
		data=resp.json()
		#print(data)
		for i in data['reviewData']:
			permaId = i['permaId']
			for key, value in permaId.items():
				if key == "id":
					print("http://tiger.in.alcatel-lucent.com:8060/cru/"+value)					

def delete_open_review(inactive_user):
	permaId = []
	for i in inactive_user:
		url = "http://test.com/rest-service/reviews-v1/filter?creator="+i+"&author="+i+"&moderator="+i+"&reviewer="+i+"&states=Review"
		headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic Y3J1YWRtaW46Y3J1YWRtaW4='}
		resp = requests.get(url, headers=headers)
		data=resp.json()
		#print(data)
		for i in data['reviewData']:
			permaId = i['permaId']
			for key, value in permaId.items():
				if key == "id":
					load = {
					"action":"action:closeReview",
					"ignoreWarnings":"ignoreWarnings==true"
					}
					uri = "http://test.com/rest-service/reviews-v1/"+value+"/transition?action=action:closeReview"
					response = requests.post(uri, data=load, headers=headers)
					rest=response.json()
					print(rest)


activeusers = active_users_get()
reviewusers = reviews_users_get()

inactive_user = (list(set(reviewusers).difference(set(activeusers))))
inactive_user.sort()
print(inactive_user)

open_review_get(inactive_user)
delete_open_review(inactive_user)
