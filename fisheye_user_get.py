
#!/usr/bin/python3
import requests
import json
userDetail={}
def active_users_get():
	active_users = []
	#url = "http://tiger.in.alcatel-lucent.com:8091/rest/api/2/group/member"

	nextUrl=url = "http://tiger.in.alcatel-lucent.com:8091/rest/api/2/group/member?groupname=fe-cru-users&startAt=0&maxResults=500"
	while nextUrl !=None:
		query = {'startAt': 0, 'maxResults': 500, 'groupname': 'fe-cru-users'}
		headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic Y3J1YWRtaW46Y3J1YWRtaW4='}
		resp = requests.get(nextUrl,  headers=headers, params=query)
		data=json.loads(resp.text)
		#print(data["nextPage"],data)
		nextUrl=url
		for i in range(0,len(data["values"])):
			key=data["values"][i]["self"].split("=")[1]
			if key not in userDetail:
				userDetail[key]={}
			userDetail[key]["userName"]=((key))
			userDetail[key]["displayName"]=((data["values"][i]["displayName"]))
			userDetail[key]["email"]=((data["values"][i]["emailAddress"]))
		nextUrl=None
		if "nextPage" in data:
			nextUrl=data["nextPage"]
	return userDetail
print(active_users_get())



