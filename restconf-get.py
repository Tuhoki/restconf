import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.103/restconf/data/ietf-interfaces:interfaces"
headers = {"Content-type":"application/yang-data+json",
           "Accept":"application/yang-data+json"}
basicauth = ("cisco","cisco123!")
resp=requests.get(api_url,auth=basicauth,headers=headers,verify=False)
response_json = resp.json()
if resp.status_code==200:
    print(json.dumps(response_json, indent=1))
print("Hello World")
print("My name is Hoan")
